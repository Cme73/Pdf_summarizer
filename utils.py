import fitz

def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def split_text(text, max_chunk_size=1000):
    return [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
