import fitz  # PyMuPDF
import docx

def parse_document(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return parse_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return parse_docx(uploaded_file)
    else:
        return {"Raw Text": "Unsupported file format."}

def parse_pdf(file):
    file.seek(0)  # Rewind the file
    doc = fitz.open(stream=file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return {"Raw Text": full_text.strip()}

def parse_docx(file):
    doc = docx.Document(file)
    full_text = "\n".join([para.text for para in doc.paragraphs])
    return {"Raw Text": full_text.strip()}
