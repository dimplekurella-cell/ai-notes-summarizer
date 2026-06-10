import streamlit as st
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
st.set_page_config(page_title="AI Notes Summarizer", page_icon="📝")

st.title("📝 AI Notes Summarizer")
st.write("Upload a PDF or paste text to generate a summary.")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

text_input = st.text_area("Or paste your text here")

if st.button("Summarize"):


    pdf_reader = PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, 5)

    st.subheader("Summary")
    for sentence in summary:
        st.write(sentence)
    