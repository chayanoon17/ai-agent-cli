import logging
from typing import List
from classifiers.question_type import (
    is_gold_question, is_rag_question, is_wiki_question
)
from handlers.question_handler import (
    handle_gold_tool, handle_rag_tool, handle_wiki_tool, handle_general_gpt
)

def handle_question(question: str, history: List[str] = []) -> str:
    try:
        if is_gold_question(question):
            return handle_gold_tool(question)
        elif is_rag_question(question):
            return handle_rag_tool(question)
        elif is_wiki_question(question):
            return handle_wiki_tool(question)
        else:
            return handle_general_gpt(question)
    except Exception as e:
        logging.error(f" Error in handle_question: {str(e)}")
        return f" เกิดข้อผิดพลาด: {str(e)}"
