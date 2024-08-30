import os
import platform
import sys
from PIL import Image
import pytesseract
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from roi_extract import getManualRoi


def configure_tesseract():
    system = platform.system()
    if system == 'Windows':
        # Windows path settings
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
    elif system == 'Linux':
        # Linux path settings
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
        os.environ['TESSDATA_PREFIX'] = '/usr/local/share/tessdata/'
    elif system == 'Darwin':
        # macOS path settings
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
        os.environ['TESSDATA_PREFIX'] = '/usr/local/share/tessdata/'
    else:
        raise OSError("Unsupported operating system")

def extract_text_from_image(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img, lang='eng')
            pyperclip.copy(text)
            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def show_message_dialog(extracted_text, app):
    
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
    configure_tesseract()
    image_path, app = getManualRoi()
    
    extracted_text = extract_text_from_image(image_path)
    show_message_dialog(extracted_text, app)

if __name__ == "__main__":
    main()