import unittest
from unittest.mock import patch, MagicMock
from agent.decision_agent import handle_question

class TestHandleQuestion(unittest.TestCase):

    @patch("agent.decision_agent.get_gold_price", return_value="32000 บาท")
    def test_gold_price(self, mock_gold):
        result = handle_question("ราคาทองขึ้นหรือยัง")
        self.assertIn("32000", result)

    @patch("agent.decision_agent.get_wiki_summary", return_value="กรุงเทพเป็นเมืองหลวงของประเทศไทย")
    def test_wiki_summary(self, mock_wiki):
        result = handle_question("กรุงเทพอยู่ที่ประเทศอะไร?")
        self.assertIn("กรุงเทพเป็นเมืองหลวง", result)

    @patch("agent.decision_agent.ask_rag", return_value="ร้านเปิด 10 โมง")
    def test_rag(self, mock_rag):
        result = handle_question("ร้านอาหารครูต้วยเปิดกี่โมง")
        self.assertIn("ร้านเปิด 10 โมง", result)

    @patch("agent.decision_agent.llm")
    def test_gpt_fallback(self, mock_llm):
        mock_response = MagicMock()
        mock_response.content = "คำตอบจาก GPT จำลอง"
        mock_llm.invoke.return_value = mock_response

        result = handle_question("เล่าเรื่องสนุกๆ หน่อย")
        self.assertIn("คำตอบจาก GPT", result)

if __name__ == "__main__":
    unittest.main()
