import streamlit as st 
import nltk 
import pickle 
import fitz
import re 
import easyocr 
from rake_nltk import Rake 
from docx import Document 
from PIL import Image

#loading function in pickle file 
with open('keyword_extraction.pkl','rb') as file:
  loaded_extract_text_from_pdf=pickle.load(file)
  loaded_extract_keywords_from_text=pickle.load(file)
  loaded_clean_keywords=pickle.load(file)
  loaded_extract_text_from_doc=pickle.load(file)
  loaded_extract_text_from_image=pickle.load(file)
  
st.title('**********KEYWORD EXTRACTION APPLICATION***********')

#uploading the file 
uploaded_file=st.file_uploader("choose a file", type=["pdf","docx","jpeg","png","jpg"])

if uploaded_file is not None:
    file_type=uploaded_file.type.split('/')[1]
    
    if file_type == "pdf":
        pdf_text=loaded_extract_text_from_pdf(uploaded_file)
        pdf_keywords=loaded_extract_keywords_from_text(pdf_text)
        pdf_cleaned_keywords=loaded_clean_keywords(pdf_keywords)
        
        st.header("PDF TEXT")
        st.text(pdf_text)
        
        st.header("CLEANED KEYWORDS")
        st.write(pdf_cleaned_keywords)
    
    elif file_type=="docx":
        doc_text=loaded_extract_text_from_doc(uploaded_file)
        doc_keywords=loaded_extract_keywords_from_text(doc_text)
        doc_cleaned_keywords=loaded_clean_keywords(doc_keywords)
        
        st.header("WORD TEXT")
        st.text(doc_text)
        
        st.header("CLEANED KEYWORDS")
        st.write(doc_cleaned_keywords)
        
    elif file_type in ["jpeg","png","jpg"]:
        image= Image.open(uploaded_file)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)
        image_text = ' '.join([entry[1] for entry in result])
        image_keywords = loaded_extract_keywords_from_text(image_text)
        image_cleaned_keywords = loaded_clean_keywords(image_keywords)
        
        st.header("IMAGE TEXT")
        st.text(image_text)
        
        st.header("CLEANED KEYWORDS")
        st.write(image_cleaned_keywords)