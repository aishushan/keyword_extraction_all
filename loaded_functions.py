# loaded_functions.py
import pickle
import functions  # Import the functions module

with open('keyword_extraction.pkl', 'rb') as file:
    loaded_extract_text_from_pdf = functions.extract_text_from_pdf
    loaded_extract_keywords_from_text = functions.extract_keywords_from_text
    loaded_clean_keywords = functions.clean_keywords
    loaded_extract_text_from_doc = functions.extract_text_from_doc
    loaded_extract_text_from_image = functions.extract_text_from_image
