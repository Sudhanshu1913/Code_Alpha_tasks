import pytesseract
from PIL import Image
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
from spellchecker import SpellChecker

# Define the directory to save audio files
OUTPUT_AUDIO_DIRECTORY = r'D:\Captures\tesseract'

def image_to_text(image_path):
    try:
        # Use pytesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(Image.open(image_path))
    except pytesseract.TesseractError:
        extracted_text = "Text extraction failed. Unable to recognize text."

    return extracted_text

def correct_spelling(text):
    spell = SpellChecker()
    words = text.split()
    corrected_text = ' '.join([spell.correction(word) for word in words])
    return corrected_text

def text_to_speech(text, output_audio_path, lang='en-gb'):
    # Check if there is text to speak
    if text:
        # Use gTTS to convert text to speech with the specified language (accent)
        tts = gTTS(text, lang=lang)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)

        # Save the audio file
        tts.save(output_audio_path)
        print(f"Audio saved to: {output_audio_path}")
    else:
        print("No text to speak.")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        # Get the output audio file path
        file_name = os.path.splitext(os.path.basename(file_path))[0] + "_output.mp3"
        output_audio_path = os.path.join(OUTPUT_AUDIO_DIRECTORY, file_name)

        # Set the language to British English (en-gb)
        extracted_text = image_to_text(file_path)
        text_to_speech(extracted_text, output_audio_path, lang='en-gb')

if __name__ == "__main__":
    # Create a simple GUI to browse for an image and generate audio
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to upload an image
    print("Please select an image.")
    browse_image()
