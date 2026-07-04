import PyPDF2
def extraxt_text_from_pdf(pdf_file):
    """Extracts raw text strings from an uploaded PDF file buffer."""
    reader = PyPDF2.PdfReader(pdf_file)
    text = " "
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


