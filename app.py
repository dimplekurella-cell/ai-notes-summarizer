import streamlit as st

st.set_page_config(page_title="AI Notes Summarizer", page_icon="📝")

st.title("📝 AI Notes Summarizer")
st.write("Upload a PDF or paste text to generate a summary.")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

text_input = st.text_area("Or paste your text here")

if st.button("Summarize"):
    if uploaded_file:
        st.success("PDF uploaded successfully!")
        st.write("Summarization logic will be added here.")
    elif text_input:
        st.success("Text received!")
        st.write("Summarization logic will be added here.")
    else:
        st.warning("Please upload a PDF or enter some text.")