# Chatbot Model
import os
import joblib
import re
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer, util


# Load the chatbot model from the pickle file
model_data = joblib.load("C:/Users/ragu/capstone_pj/models/chatbot_model.pkl")

# Extract components
qa_pairs = model_data["qa_pairs"]
question_embeddings = model_data["question_embeddings"]
model_name = model_data["model_name"]

# Load the SentenceTransformer model
model = SentenceTransformer(model_name)

# Chat function
def chat_with_bot(user_input):
    input_embedding = model.encode(user_input)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    best_match_idx = similarities.argmax()
    return qa_pairs[best_match_idx]["answer"]

# Streamlit UI
st.set_page_config(page_title="Insurance Chatbot", page_icon="💬")

st.title("💬 Insurance Chatbot")
st.write("Ask me anything about insurance (health, life, motor, or home).")

# Input box
user_input = st.text_input("You:", "")

if user_input:
    response = chat_with_bot(user_input)
    st.markdown("**Bot:** " + response)

