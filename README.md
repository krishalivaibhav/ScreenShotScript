# Screenshot Text Extractor with Clipboard Automation

This project is a Python-based tool that uses Tesseract OCR to automatically extract text from any screenshot taken and copy it directly to the clipboard for easy access. Designed to streamline workflows, this tool eliminates the need for manual text transcription from images, making digital documentation faster and more efficient.

## Features
- **Automated Text Extraction**: Instantly extracts text from screenshots, reducing the need for manual text entry and transcription.
- **Clipboard Integration**: After extracting text, the tool automatically copies it to the clipboard, allowing for quick pasting into other applications.
- **High Accuracy with Tesseract OCR**: Leverages the robust Tesseract OCR engine to recognize and convert text from screenshots accurately, handling a variety of fonts, sizes, and layouts.
- **Image Pre-Processing for Enhanced OCR Performance**: Utilizes OpenCV for image enhancement techniques like resizing, thresholding, and noise reduction to improve OCR accuracy across different screenshot formats.
- **User-Friendly and Efficient**: Requires minimal user input, making it accessible and easy to integrate into everyday workflows.

## How It Works
1. **Screenshot Capture**: When a screenshot is taken, the tool captures the image file.
2. **Text Recognition**: Tesseract OCR processes the image, recognizing and extracting text content.
3. **Clipboard Copy**: The extracted text is automatically copied to the clipboard, allowing the user to paste it wherever needed.

## Requirements
- Python 3.x
- Tesseract OCR
- OpenCV
- Pyperclip (for clipboard functionality)

## Usage
1. Install the dependencies listed in `requirements.txt`.
2. Run the script and take a screenshot.
3. The text from the screenshot will be available in your clipboard, ready to paste.
