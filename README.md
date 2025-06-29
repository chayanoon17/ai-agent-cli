# 🤖 AI Agent CLI

ระบบ AI Agent แบบ CLI (Command Line Interface) ที่สามารถตอบคำถามผู้ใช้ผ่าน Terminal โดยเลือกใช้ Tool อย่างชาญฉลาด เช่น:

- 📄 ข้อมูลเฉพาะจาก RAG (ร้านครูต้วย)
- 🌐 ข้อมูลจาก Wikipedia
- 🪙 ราคาทองคำล่าสุด
- 💬 ตอบทั่วไปด้วย GPT-3.5

---

## ⚙️ Stack ที่ใช้

| ส่วน                | รายละเอียด                              |
|---------------------|-------------------------------------------|
| Language            | Python 3.10+                              |
| LLM                 | OpenAI GPT-3.5 Turbo                      |
| Tool Integration    | LangChain, Wikipedia API, Custom Tools    |
| Vector Store        | FAISS (สำหรับ RAG)                        |
| Env Manager         | `python-dotenv`                           |
| Interface           | CLI (`main.py`)                           |

---

## ▶️ วิธีรันโปรเจกต์

### 1. Clone โปรเจกต์

```bash
git clone https://github.com/yourname/ai-agent-cli.git
cd ai-agent-cli
```

### 2. สร้าง Virtual Environment และ Activate

```bash
python -m venv .venv
source .venv/bin/activate # บน Windows ใช้ .venv\Scripts\activate
```

### 3. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 4. สร้างไฟล์ `.env` และใส่ API Key

```env
OPENAI_API_KEY=your_openai_key_here
```

### 5. รัน Agent

```bash
python main.py
```

จากนั้นพิมพ์คำถาม เช่น:

- `ราคาทองวันนี้`
- `กรุงเทพคืออะไร`
- `ร้านครูต้วยเปิดกี่โมง`
- `AI คืออะไร`

---

## 🔌 วิธีเพิ่ม Tool ใหม่

หากต้องการให้ Agent ตอบคำถามเฉพาะทาง เช่น ราคาน้ำมัน, พยากรณ์อากาศ ฯลฯ:

### 1. เพิ่มฟังก์ชันใน `tools/` เช่น `oil_tool.py`

```python
def get_oil_price():
    return "ราคาน้ำมันวันนี้คือ 35.99 บาท/ลิตร"
```

### 2. เพิ่ม logic ตรวจจับคำถามใน `classifiers/question_type.py`

```python
def is_oil_question(question: str) -> bool:
    return "น้ำมัน" in question
```

### 3. เพิ่ม handler ใน `handlers/question_handler.py`

```python
from tools.oil_tool import get_oil_price

def handle_oil_tool(question: str) -> str:
    return f"[⛽️ Oil] {get_oil_price()}"
```

### 4. เพิ่ม routing ใน `agent/decision_agent.py`

```python
if is_oil_question(question):
    return handle_oil_tool(question)
```

---

## 🧠 แนวคิดของ Agent / Decision Logic

Agent ใช้แนวคิด **"Tool-based Reasoning"** โดยแบ่งการตัดสินใจออกเป็น 4 ขั้นตอนหลัก:

1. **Classification**: ตรวจสอบประเภทคำถาม เช่น ทอง, wiki, rag, หรือทั่วไป
2. **Tool Selection**: เลือกเครื่องมือ (Tool) ที่เหมาะสม
3. **Tool Execution**: เรียกใช้งาน Tool นั้นเพื่อดึงคำตอบ
4. **Fallback**: หากไม่เข้าเงื่อนไขใดเลย → ใช้ GPT-3.5 ตอบแทน

> ระบบถูกออกแบบให้ **ขยายง่าย** โดยแยกส่วน `classifiers`, `handlers`, และ `tools` ออกจากกันอย่างเป็นระเบียบ

---


## วิธีเพิ่มไฟล์เข้า RAG Agent

ระบบนี้ใช้ FAISS เป็น Vector Store และมักใช้ rag/docs สำหรับเก็บเอกสาร

1. เตรียมไฟล์ข้อมูล
รูปแบบที่รองรับ: .txt, .pdf, .md, .csv หรือ .docx

ตัวอย่างเช่น docs/ร้านครูต้วย.txt (ผมได้เพิ่มไฟส์ pdf ไว้ 1 ไฟส์แล้ว)

รันไฟล์เพื่อสร้างฐานข้อมูล RAG: 
```bash
    python rag/ingest_docs.py
```

----

## 📘 สิ่งที่เรียนรู้ / ท้าทาย

- ✅ การใช้ LangChain เพื่อเชื่อมต่อ LLM และ Tool ได้อย่างยืดหยุ่น
- ✅ การวางโครงสร้างโค้ดให้ขยายและดูแลง่ายในระยะยาว
- ✅ การใช้ FAISS Vector Store สำหรับ Retrieval-Augmented Generation (RAG)
- 🧠 ความท้าทาย: การตั้งเกณฑ์คำถามให้ Tool ทำงานแม่นยำ
- 🧪 มีการเขียน Unit Test เพื่อทดสอบ logic และ decision flow อย่างเป็นระบบ

---

ขอบคุณสำหรับโอกาสน่ะครับผม 
