# summarizer_utils.py
from transformers import pipeline

def summarize_text(text_list):
    summarizer = pipeline("summarization", model="t5-small")
    return [summarizer(text, max_length=200, min_length=50, do_sample=False)[0]["summary_text"]
            for text in text_list]