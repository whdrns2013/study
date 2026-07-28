# _get_yf_stock_info.py
import yfinance as yf

def func(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    return str(info)

tool_def = {
        "type": "function",
        "function": {
            "name": "get_yf_stock_info",
            "description": "해당 종목의 Yahoo Finance 정보를 반환합니다.",
            "parameters": {
                "type":"object",
                "properties":{
                    "ticker": {
                        "type":"string",
                        "description":"Yahoo Finance 정보를 반환할 종목의 티커를 입력하세요. (예:APPL)",
                    }
                },
                "required":["ticker"]
            }
        }
    }