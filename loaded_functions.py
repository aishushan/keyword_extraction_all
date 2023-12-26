# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:25:23 2023

@author: Aiswarya
"""

import pickle
from functions import extract_text_from_pdf, extract_keywords_from_text, clean_keywords, extract_text_from_doc, extract_text_from_image

with open('keyword_extraction.pkl', 'rb') as file:
    loaded_extract_text_from_pdf = pickle.load(file)
    loaded_extract_keywords_from_text = pickle.load(file)
    loaded_clean_keywords = pickle.load(file)
    loaded_extract_text_from_doc = pickle.load(file)
    loaded_extract_text_from_image = pickle.load(file)

# Your code to use loaded functions
