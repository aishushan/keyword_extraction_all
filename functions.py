# functions.py
import pickle
from docx import Document
import fitz
import nltk 
import re
import easyocr
from rake_nltk import Rake
from PIL import Image
import nltk
import io
from docx import Document


# Download the stopwords resource
nltk.download('stopwords')
nltk.download('punkt')


def extract_keywords_with_rake(text):
    # Print debug information
    print("Text for Keyword Extraction:", text)

    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases_with_scores()

    # Print debug information
    print("Extracted Keywords:")
    for score, phrase in keywords:
        print(f"{score}: {phrase}")

    return keywords


def extract_text_from_pdf(uploaded_file):
    try:
        # Save the uploaded file temporarily
        with open("temp_pdf.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Print debug information
        print("Uploaded File Name:", uploaded_file.name)
        print("Uploaded File Type:", uploaded_file.type)

        # Open and extract text
        text = ""
        with fitz.open("temp_pdf.pdf") as doc:
            for page_num in range(doc.page_count):
                page = doc[page_num]
                text += page.get_text("text")

        # Print debug information
        print("Extracted Text from PDF:", text)

        return text
    except Exception as e:
        # Print debug information
        print("Error in extract_text_from_pdf:", str(e))
        return None

def extract_text_from_doc(uploaded_file):
    try:
        # Print debug information
        print("Uploaded File Name:", uploaded_file.name)
        print("Uploaded File Type:", uploaded_file.type)

        # Create a BytesIO object from the buffer
        file_buffer = io.BytesIO(uploaded_file.read())

        # Extract text using python-docx
        doc = Document(file_buffer)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

        # Print debug information
        print("Extracted Text from DOCX:", text)

        return text
    except Exception as e:
        # Print debug information
        print("Error in extract_text_from_doc:", str(e))
        return None

def extract_keywords_from_text(text):
    try:
        # Print debug information
        print("Text for Keyword Extraction:", text)

        # Initialize Rake
        r = Rake()

        # Extract keywords
        r.extract_keywords_from_text(text)
        keywords = r.get_ranked_phrases_with_scores()

        # Print debug information
        print("Extracted Keywords:")
        for score, phrase in keywords:
            print(f"{score}: {phrase}")

        return keywords

    except Exception as e:
        # Print debug information
        print("Error in extract_keywords_from_text:", str(e))
        return None

def clean_keywords(keywords):
    cleaned_keywords = [(score, re.sub(r'[^a-zA-Z0-9\s]', '', phrase)) for score, phrase in keywords]

    # Print debug information
    print("Cleaned Keywords:", cleaned_keywords)

    return cleaned_keywords


def extract_text_from_image(uploaded_file):
    # Print debug information
    print("Uploaded File Name:", uploaded_file.name)
    print("Uploaded File Type:", uploaded_file.type)

    # Save the uploaded file temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text from image
    reader = easyocr.Reader(['en'])
    result = reader.readtext("temp_image.jpg")
    text = ' '.join([entry[1] for entry in result])

    # Print debug information
    print("Extracted Text from Image:", text)

    return text
