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


def configure_tesseract():
    """
    Configures the tesseract ocr engine path on host system depending on OS.
    TODO: bundles the tesseract ocr engine into the application.
    Raises:
        OSError: only supports linux, windows, and mac-os
    """
    system = platform.system()
    if system == "Windows":
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )
        os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"
    elif system == "Linux":
        pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
        os.environ["TESSDATA_PREFIX"] = "/usr/local/share/tessdata/"
    elif system == "Darwin":
        pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
        os.environ["TESSDATA_PREFIX"] = "/usr/local/share/tessdata/"
    else:
        raise OSError("Unsupported operating system")


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
