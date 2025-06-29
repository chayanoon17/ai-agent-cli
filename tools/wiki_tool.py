import wikipedia

def get_wiki_summary(query: str, lang: str = "th") -> str:
    """
    ดึงสรุปข้อมูลจาก Wikipedia ตามคำค้น query
    """
    wikipedia.set_lang(lang)
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"คำค้น '{query}' ไม่ชัดเจน: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return f"ไม่พบหน้าบทความสำหรับ '{query}'"
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"
