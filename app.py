import streamlit as st
import nltk
import ollama
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator
st.set_page_config(page_title="AI Notes Summarizer", page_icon="📝")
def summarize_with_ollama(text):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following text in simple bullet points:\n\n{text}"
            }
        ]
    )
    return response["message"]["content"]
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

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

        summary = summarize_with_ollama(text)

        if language != "English":
            summary = GoogleTranslator(
                source="auto",
                target=lang_map[language]
            ).translate(summary)

        st.subheader("AI Summary")
        st.write(summary)

    elif text_input:
        summary = summarize_with_ollama(text_input)

        if language != "English":
            summary = GoogleTranslator(
                source="auto",
                target=lang_map[language]
            ).translate(summary)

        st.subheader("AI Summary")
        st.write(summary)

    else:
        st.warning("Please upload a PDF or enter some text.")