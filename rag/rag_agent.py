# rag/rag_agent.py

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

def ask_rag(question: str) -> str:
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = FAISS.load_local("rag/faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join(doc.page_content for doc in docs)

    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        SystemMessage(content="คุณคือผู้ช่วยที่ตอบคำถามจากเอกสารด้านล่างอย่างถูกต้องและกระชับ"),
        HumanMessage(content=f"เอกสาร:\n{context}\n\nคำถาม: {question}")
    ]

    response = llm.invoke(messages)
    return response.content
