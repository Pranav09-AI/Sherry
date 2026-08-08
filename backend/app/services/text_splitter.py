from app.services.document_loader import load_path,load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = load_pdf(load_path)

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 100,
        chunk_overlap = 10,
        length_function = len,
        is_separator_regex=False,
    )

    return text_splitter.split_documents(documents)