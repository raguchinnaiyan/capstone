import os
import joblib
import re
import numpy as np
import streamlit as st
from textblob import TextBlob


# Set page title
st.set_page_config(page_title="Insurance Sentiment Analyzer", layout="centered",page_icon="🎭")

# App heading
st.title("🧠 Insurance Feedback Sentiment Analyzer")

# Define stop words
stop_words = set([
    'the', 'and', 'is', 'in', 'it', 'of', 'to', 'a', 'for', 'on', 'this', 'that',
    'with', 'as', 'was', 'but', 'are', 'have', 'be', 'at', 'or', 'an', 'so',
    'if', 'out', 'not'
])

# Define function for cleaning and analysis
def sentiment_analysis(raw_text):
    lower = raw_text.lower()
    special = re.sub(r"[^a-zA-Z0-9]", " ", lower)
    tokens = special.split()
    tokens = [word for word in tokens if word not in stop_words]
    cleaned_text = " ".join(tokens)

    # Use TextBlob for sentiment
    polarity = TextBlob(cleaned_text).sentiment.polarity
    if polarity > 0.1:
        return "😊 Positive"
    elif polarity < -0.1:
        return "😞 Negative"
    else:
        return "😐 Neutral"

# Text input from user
user_input = st.text_area("✍️ Enter customer feedback about insurance:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        result = sentiment_analysis(user_input)
        st.subheader("Sentiment:")
        st.success(result)
