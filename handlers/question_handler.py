import logging
import re
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI
from tools.gold_tool import get_gold_price
from tools.wiki_tool import get_wiki_summary
from rag.rag_agent import ask_rag
import os

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def handle_gold_tool(question: str) -> str:
    logging.info("Using Gold Price Tool")
    return f"[🪙 Gold] ราคาทองคำวันนี้คือ: {get_gold_price()}"

def handle_wiki_tool(question: str) -> str:
    logging.info("Using Wikipedia Tool")
    question = re.sub(r"(wiki(pedia)?[:：]?\s*)", "", question, flags=re.IGNORECASE)
    question = re.sub(r"(|คือใคร|อยู่ที่ประเทศอะไร|ข้อมูลเกี่ยวกับ|ประวัติของ|ข้อมูลของ)", "", question, flags=re.IGNORECASE)
    cleaned_query = question.strip()

    summary = get_wiki_summary(cleaned_query)
    if "ไม่พบ" in summary or len(summary.strip()) == 0:
        return f"[🌐 Wiki] ไม่พบข้อมูลใน Wikipedia สำหรับ '{cleaned_query}'"
    return f"[🌐 Wiki] สรุปจาก Wikipedia: {summary}"

def handle_rag_tool(question: str) -> str:
    logging.info("Using RAG Tool")
    return f"[📄 RAG] {ask_rag(question)}"

def handle_general_gpt(question: str) -> str:
    logging.info("Using GPT-3.5 Fallback")
    response = llm.invoke([
        HumanMessage(content=f"ผู้ใช้ถามว่า: {question} กรุณาตอบแบบมืออาชีพ")
    ])
    return f"🤖 GPT-3.5: {response.content}"
