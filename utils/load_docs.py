import pandas as pd
from PyPDF2 import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_csv(index=False)