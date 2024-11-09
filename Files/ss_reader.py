import time
from PIL import ImageGrab, Image
import pytesseract
import pyperclip
import os

# Set the path to the Tesseract executable (use relative path or system PATH)
# If Tesseract is in the system PATH, you don't need to specify the full path
# Otherwise, you can specify the path relative to this script or use an environment variable
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this if needed
if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    print("Tesseract executable not found. Ensure it's installed and the path is correct.")

def capture_and_extract_text():
    # Capture a screenshot from the clipboard
    screenshot = ImageGrab.grabclipboard()

    # Check if a screenshot is available
    if isinstance(screenshot, Image.Image):
        # Use pytesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(screenshot)

        # Copy the extracted text to clipboard
        pyperclip.copy(extracted_text)
        print("Text has been copied to the clipboard.")
    else:
        print("No image found in the clipboard.")

def monitor_clipboard():
    print("Monitoring clipboard for screenshots...")
    last_image = None  # Variable to keep track of the last image
    while True:
        screenshot = ImageGrab.grabclipboard()

        # Check if there's a new image in the clipboard
        if isinstance(screenshot, Image.Image) and screenshot != last_image:
            last_image = screenshot  # Update the last image reference
            capture_and_extract_text()  # Run the extraction function

        time.sleep(1)  # Check every second

if __name__ == "__main__":
    monitor_clipboard()  # Start monitoring the clipboard
