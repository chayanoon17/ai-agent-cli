import json

def get_gold_price() -> str:
    """Mock ราคาทองคำ"""
    # JSON จำลองจาก API
    mock_data = """
    {
      "data": {
        "success": true,
        "timestamp": 1751140740,
        "date": "2025-06-28",
        "base": "USD",
        "rates": {
          "XAU": 0.000305421,
          "USDXAU": 3274.16909773722
        }
      }
    }
    """
    data = json.loads(mock_data)
    gold_price = data["data"]["rates"]["USDXAU"]
    return f"ราคาทองคำวันนี้คือ ${gold_price:,.2f} USD"
