import streamlit as st
from deep_translator import GoogleTranslator
import os
import tempfile
import PyPDF2
import docx
import io


# Function to extract text

def extract_text(file) -> str:
    file_type = file.name.split('.')[-1].lower()

    if file_type == 'txt':
        return file.read().decode("utf-8")

    elif file_type == 'pdf':
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    elif file_type == 'docx':
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])

    else:
        return None


# Translate Function

def translate_text(text, src_lang, dest_langs):
    results = {}
    for lang in dest_langs:
        translated = GoogleTranslator(source=src_lang, target=lang).translate(text)
        results[lang] = translated
    return results


# Language map

language_map = {
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn"
}


# Streamlit UI

st.set_page_config(page_title="Insurance Translator", page_icon="🌐")
st.title("🌐 Insurance Document Translator")

st.markdown("""
👋 Welcome to the **Insurance Translation Tool**!

📄 Upload a `.txt`, `.pdf`, or `.docx` insurance file and choose your desired output language.  
We'll translate your document and display the translated result instantly! 🚀
""")

uploaded_file = st.file_uploader("Upload your insurance document", type=["txt", "pdf", "docx"])
selected_lang = st.selectbox("🌍 Select target language", list(language_map.keys()))

if st.button("Translate"):
    if uploaded_file:
        try:
            # Extract text based on file type
            extracted_text = extract_text(uploaded_file)

            if not extracted_text:
                st.error("❌ Could not extract text from this file type.")
            else:
                # Perform translation
                result = translate_text(extracted_text, src_lang="en", dest_langs=[language_map[selected_lang]])
                st.subheader(f"✅ Translated Text in {selected_lang}:")
                st.success(result[language_map[selected_lang]])
        except Exception as e:
            st.error(f"⚠️ Translation failed: {e}")
    else:
        st.warning("📂 Please upload a valid file (.txt, .pdf, or .docx).")
