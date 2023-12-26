# extraction.py
import streamlit as st
from loaded_functions import loaded_extract_text_from_pdf, loaded_extract_keywords_from_text, loaded_clean_keywords, loaded_extract_text_from_doc, loaded_extract_text_from_image

st.title('**********KEYWORD EXTRACTION APPLICATION***********')

# Uploading the file
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "jpeg", "png", "jpg"])

if uploaded_file is not None:
    file_type = uploaded_file.type.split('/')[1]

    # Debugging: Print the uploaded file name and type
    st.write(f"Uploaded File Name: {uploaded_file.name}")
    st.write(f"File Type: {file_type}")

    if file_type == "pdf":
        # Use the correct function name 'loaded_extract_text_from_pdf'
        pdf_text = loaded_extract_text_from_pdf(uploaded_file)
        pdf_keywords = loaded_extract_keywords_from_text(pdf_text)
        pdf_cleaned_keywords = loaded_clean_keywords(pdf_keywords)

        st.header("PDF TEXT")
        st.text(pdf_text)

        st.header("CLEANED KEYWORDS")
        st.write(pdf_cleaned_keywords)

    elif file_type == "docx":
        # Use the correct function name 'loaded_extract_text_from_doc'
        doc_text = loaded_extract_text_from_doc(uploaded_file)
        doc_keywords = loaded_extract_keywords_from_text(doc_text)
        doc_cleaned_keywords = loaded_clean_keywords(doc_keywords)

        st.header("WORD TEXT")
        st.text(doc_text)

        st.header("CLEANED KEYWORDS")
        st.write(doc_cleaned_keywords)

    elif file_type in ["jpeg", "png", "jpg"]:
        # Use the correct function name 'loaded_extract_text_from_image'
        image_text = loaded_extract_text_from_image(uploaded_file)
        image_keywords = loaded_extract_keywords_from_text(image_text)
        image_cleaned_keywords = loaded_clean_keywords(image_keywords)

        st.header("IMAGE TEXT")
        st.text(image_text)

        st.header("CLEANED KEYWORDS")
        st.write(image_cleaned_keywords)
