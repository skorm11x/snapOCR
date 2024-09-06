"""
    Driver code for snapOCR found in main(). 
    Flow:
    1. Acquire region of interest
    2. Process through OCR engine
    3. Utilize results
"""

import os
import platform
import sys
from PIL import Image  # type: ignore
import pytesseract  # type: ignore
import pyperclip  # type: ignore
from PyQt5.QtWidgets import QApplication, QMessageBox
from roi_extract import get_manual_roi


def get_base_path():
    """returns different base filepaths depending if ran
    as executable or a script

    Returns:
        str: base filepath for application execution
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable), True
    else:
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
    if system == "Windows":
        bundled_path = os.path.join(base_path, "bin", "tesseract.exe")
        default_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.pytesseract.tesseract_cmd = (
            bundled_path if os.path.exists(bundled_path) else default_path
        )
        if os.path.exists(bundled_path):
            os.environ["TESSDATA_PREFIX"] = os.path.join(parent_path, "tessdata")
        else:
            if is_binary_exec:
                os.environ["TESSDATA_PREFIX"] = os.path.join(parent_path, "tessdata")
            else:
                os.environ["TESSDATA_PREFIX"] = os.path.join(base_path, "tessdata")
    elif system == "Linux" or system == "Darwin":
        bundled_path = os.path.join(base_path, "bin", "tesseract")
        default_path = "/usr/local/bin/tesseract"
        pytesseract.pytesseract.tesseract_cmd = (
            bundled_path if os.path.exists(bundled_path) else default_path
        )
        if os.path.exists(bundled_path):
            os.environ["TESSDATA_PREFIX"] = os.path.join(parent_path, "tessdata")
        else:
            if is_binary_exec:
                os.environ["TESSDATA_PREFIX"] = os.path.join(parent_path, "tessdata")
            else:
                os.environ["TESSDATA_PREFIX"] = os.path.join(base_path, "tessdata")
    else:
        raise OSError("Unsupported operating system")

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


def main():
    """
    The basic functionality and workflow for snapOCR.
    """
    configure_tesseract()
    app = QApplication(sys.argv)
    image_path = get_manual_roi(app)

    extracted_text = extract_text_from_image(image_path)
    show_message_dialog(extracted_text)


if __name__ == "__main__":
    main()
