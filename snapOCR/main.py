"""Run a background process to wait for keyboard trigger or allow user to invoke via cli
for single OCR window.
"""

import os
import platform
import sys
from subprocess import Popen
from pynput import keyboard
from PIL import Image  # type: ignore
import pytesseract  # type: ignore
import pyperclip  # type: ignore
from PyQt5.QtWidgets import QApplication, QMessageBox
from snapOCR.roi_extract import get_manual_roi

DEBUG = False


def get_base_path():
    """returns different base filepaths depending if ran
    as executable or a script

    Returns:
        str: base filepath for application execution
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable), True
    return os.path.dirname(os.path.abspath(__file__)), False


def configure_tesseract():
    """
    Configures the tesseract ocr engine path on host system depending on OS.
    TODO: bundles the tesseract ocr engine into the application.
    Raises:
        OSError: only supports linux, windows, and mac-os
    """
    base_path, is_binary_exec = get_base_path()
    parent_path = os.path.dirname(base_path)
    system = platform.system()

    config = {
        "Windows": {
            "bundled_path": os.path.join(base_path, "bin", "tesseract.exe"),
            "default_path": r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        },
        "Linux": {
            "bundled_path": os.path.join(base_path, "bin", "tesseract"),
            "default_path": "/usr/local/bin/tesseract",
        },
        "Darwin": {
            "bundled_path": os.path.join(base_path, "bin", "tesseract"),
            "default_path": "/opt/homebrew/bin/tesseract",
        }
    }

    if system not in config:
        raise OSError("Unsupported operating system")

    bundled_path = config[system]["bundled_path"]
    default_path = config[system]["default_path"]

    if os.path.exists(bundled_path):
        pytesseract.pytesseract.tesseract_cmd = bundled_path
    else:
        pytesseract.pytesseract.tesseract_cmd = default_path

    if os.path.exists(bundled_path):
        os.environ["TESSDATA_PREFIX"] = os.path.join(parent_path, "tessdata")
    else:
        if is_binary_exec:
            os.environ["TESSDATA_PREFIX"] = os.path.join(parent_path)
        else:
            os.environ["TESSDATA_PREFIX"] = os.path.join(base_path, "tessdata")

    if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
        raise OSError(
            f"Tesseract executable not found at {pytesseract.pytesseract.tesseract_cmd}"
        )


def extract_text_from_image(image_path):
    """
    Extracts text a screenshot saved into a temporary application file.
    Args:
        image_path (png): the screenshot, or roi, capture path

    Returns:
        str, None: returns the text as a formatted string or None
    """
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img, lang="eng")
            pyperclip.copy(text)
            return text
    except (FileNotFoundError, OSError) as e:
        print(f"An error occurred: {e}")
        return None


def show_message_dialog(extracted_text):
    """
    Shows a dialog box confirming that text has been captured to
    the clipboard or if no text was found.
    TODO: change QApplication init to belong to main.
    Args:
        extracted_text (str): the extracted text in formatted form
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    if extracted_text:
        msg.setText("Text has been copied to clipboard.")
        msg.setWindowTitle("Text Captured")
    else:
        msg.setText("No text could be extracted.")
        msg.setWindowTitle("No Capture")

    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def system_watch():
    """
    Main system_watch process that runs forever. When key press triggers.
    """
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

HOTKEY_MODIFIERS = {
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
}
HOTKEY_CHAR = "s"
pressed_keys = set()


def _hotkey_pressed(key):
    if not isinstance(key, keyboard.KeyCode):
        return False
    if not key.char:
        return False

    ctrl_pressed = any(mod in pressed_keys for mod in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r))
    alt_pressed = any(mod in pressed_keys for mod in (keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r))
    return ctrl_pressed and alt_pressed and key.char.lower() == HOTKEY_CHAR


def on_press(key):
    """Callback function that detects the hotkey combo and triggers snapOCR."""
    pressed_keys.add(key)
    try:
        if DEBUG:
            print(f'key pressed: {key} ({type(key)})')
            if key == keyboard.Key.esc:
                print('Escape pressed, exiting watcher')
                sys.exit()
        if _hotkey_pressed(key):
            print(f"hotkey pressed: {key}")
            invoke_snapocr()
        elif DEBUG:
            print("hotkey not matched")
    except AttributeError:
        if DEBUG:
            print("Received non-standard key event")
        pass


def on_release(key):
    pressed_keys.discard(key)


def invoke_snapocr():
    """Starts snapOCR as a separate subprocess."""
    python_executable = sys.executable
    with Popen([python_executable, "-m", "snapOCR.main", "--snapocr"]):
        pass


def snapocr_main():
    """The snapOCR process workflow."""
    configure_tesseract()
    app = QApplication(sys.argv)
    image_path = get_manual_roi(app)
    extracted_text = extract_text_from_image(image_path)
    show_message_dialog(extracted_text)


if __name__ == "__main__":
    if "--debug" in sys.argv:
        DEBUG = True
        print("debug started for snapOCR")
    if "--snapocr" in sys.argv:
        snapocr_main()
    else:
        system_watch()
