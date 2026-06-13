import streamlit as st
import nltk
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator
st.set_page_config(page_title="AI Notes Summarizer", page_icon="📝")
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Google API Key not found. Please configure GOOGLE_API_KEY.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_with_ai(text):
    prompt = f"""
    Summarize the following text in simple bullet points:

    {text}
    """

    response = model.generate_content(prompt)
    return response.text
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


st.title("📝 AI Notes Summarizer")
st.write("Upload a PDF or paste text to generate a summary.")
language = st.selectbox(
    "Select Output Language",
    ["English", "Hindi", "Telugu", "Tamil", "Kannada"]
)

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

text_input = st.text_area("Or paste your text here")

if st.button("Summarize"):
    lang_map = {
        "English": "en",
        "Hindi": "hi",
        "Telugu": "te",
        "Tamil": "ta",
        "Kannada": "kn"
    }

    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        text = ""

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        summary = summarize_with_ai(text)

        if language != "English":
            summary = GoogleTranslator(
                source="auto",
                target=lang_map[language]
            ).translate(summary)

        st.subheader("AI Summary")
        st.write(summary)

    elif text_input:
        summary = summarize_with_ai(text_input)

        if language != "English":
            summary = GoogleTranslator(
                source="auto",
                target=lang_map[language]
            ).translate(summary)

        st.subheader("AI Summary")
        st.write(summary)

    else:
        st.warning("Please upload a PDF or enter some text.")