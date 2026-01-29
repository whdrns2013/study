# _get_yf_stock_history.py
import yfinance as yf

def func(ticker:str, period:str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return str(hist.to_markdown())

tool_def = {
        "type": "function",
        "function": {
            "name": "get_yf_stock_history",
            "description": "해당 종목의 Yahoo Finance 주가 정보를 반환합니다.",
            "parameters": {
                "type":"object",
                "properties":{
                    "ticker": {
                        "type":"string",
                        "description":"Yahoo Finance 주가 정보를 반환할 종목의 티커를 입력하세요. (예:APPL)",
                    },
                    "period": {
                        "type": "string",
                        "description":"주가 정보를 조회할 기간을 입력하세요. (예: 1d, 5d, 1mo, 3mo, 1y, 5y)"
                    }
                },
                "required":["ticker", "period"]
            }
        }
    }