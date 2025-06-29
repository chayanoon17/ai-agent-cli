# build_index.py
from dotenv import load_dotenv
load_dotenv()  # ✅ โหลด .env เข้า environment

from rag.vector_store import build_faiss_index

if __name__ == "__main__":
    build_faiss_index()
    print("✅ ฝังเวกเตอร์จาก PDF สำเร็จแล้ว")
