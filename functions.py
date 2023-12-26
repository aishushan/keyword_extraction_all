import pickle
from docx import Document
import fitz
import re
import easyocr
from rake_nltk import Rake
from PIL import Image

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text("text.utf8").replace('\uFFFD', 't')
    return text

# Function to extract keywords from text
def extract_keywords_from_text(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases_with_scores()
    return keywords

# Function to clean keywords
def clean_keywords(keywords):
    cleaned_keywords = [(score, re.sub(r'[^a-zA-Z0-9\s]', '', phrase)) for score, phrase in keywords]
    return cleaned_keywords

# Function to extract text from Word document
def extract_text_from_doc(doc_path):
    doc = Document(doc_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to extract text from image
def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    text = ' '.join([entry[1] for entry in result])
    return text


