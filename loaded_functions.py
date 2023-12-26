# loaded_functions.py
import pickle
from functions import extract_text_from_pdf, extract_keywords_from_text, clean_keywords, extract_text_from_doc, extract_text_from_image

with open('keyword_extraction.pkl', 'rb') as file:
    loaded_extract_text_from_pdf = extract_text_from_pdf
    loaded_extract_keywords_from_text = extract_keywords_from_text
    loaded_clean_keywords = clean_keywords
    loaded_extract_text_from_doc = extract_text_from_doc
    loaded_extract_text_from_image = extract_text_from_image
