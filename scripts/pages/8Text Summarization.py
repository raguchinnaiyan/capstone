
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from transformers import pipeline
import streamlit as st

# 1. Redefine the function exactly as it was used
def summarize_text(text_list):
    summarizer = pipeline("summarization", model="t5-small")  
    return [summarizer(text, max_length=200, min_length=50, do_sample=False)[0]["summary_text"]
            for text in text_list]

# 2. Set up Streamlit UI
st.set_page_config(page_title="Text Summarizer", page_icon="📝")
st.title("📝 Insurance Text Summarization")

st.markdown("Upload a text file or paste your text, and get a concise summary using a transformer model.")

# 3. Choose input method
input_option = st.radio("Choose input method:", ["Paste Text", "Upload .txt File"])

user_text = ""

if input_option == "Paste Text":
    user_text = st.text_area("Paste your text here")
elif input_option == "Upload .txt File":
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        user_text = uploaded_file.read().decode("utf-8")

# 4. Summarize button
if st.button("Summarize"):
    if user_text.strip():
        # ✅ 5. Load model *after* defining the function
        summarizer_model = joblib.load("C:/Users/ragu/capstone_pj/scripts/models/text_summarization1.pkl")

        try:
            summary = summarizer_model.transform([user_text])
            st.subheader("Summary:")
            st.write(summary[0])
        except Exception as e:
            st.error(f"Failed to summarize: {e}")
    else:
        st.warning("Please paste some text or upload a file.")
