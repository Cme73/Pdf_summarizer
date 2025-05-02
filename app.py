import streamlit as st
from utils import extract_text_from_pdf, split_text
from summarizer import summarize_text

st.title("📄 PDF Summarizer App")

pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

if pdf_file is not None:
    st.info("📚 Extracting text...")
    raw_text = extract_text_from_pdf(pdf_file)

    st.info("✂️ Splitting into chunks...")
    chunks = split_text(raw_text)

    st.success("✅ Summarizing...")
    full_summary = ""

    for chunk in chunks:
        full_summary += summarize_text(chunk) + "\n\n"

    st.subheader("📝 Summary")
    st.write(full_summary)
