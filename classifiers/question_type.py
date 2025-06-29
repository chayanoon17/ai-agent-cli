import re
from difflib import SequenceMatcher
from rag.rag_phrases import rag_phrases

def is_gold_question(question: str) -> bool:
    return bool(re.search(r"(ราคาทอง|ทองคำ)", question))

def is_wiki_question(question: str) -> bool:
    return bool(re.search(r"(wiki(pedia)?|คือใคร|ประวัติ|ข้อมูล|อยู่ที่ประเทศอะไร)", question, re.IGNORECASE))

def is_rag_question(question: str) -> bool:
    return any(SequenceMatcher(None, question.lower(), kw.lower()).ratio() > 0.7 for kw in rag_phrases)
