import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from rag.load_docs import load_and_split_all_pdfs

def build_faiss_index():
    docs = load_and_split_all_pdfs("rag/docs")
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("rag/faiss_index")
    print("✅ ฝังเวกเตอร์จาก PDF หลายไฟล์สำเร็จแล้ว")
