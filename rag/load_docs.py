import os
from langchain_community.document_loaders import PyPDFLoader

def load_and_split_all_pdfs(directory: str):
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(directory, filename))
            docs.extend(loader.load())
    return docs
