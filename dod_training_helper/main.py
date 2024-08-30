from PIL import Image
import pytesseract
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = 'Capture.png'
    
    extracted_text = extract_text_from_image(image_path)
    
    if extracted_text:
        pyperclip.copy(extracted_text)
        print("Extracted text copied to clipboard.")
    else:
        print("No text could be extracted.")