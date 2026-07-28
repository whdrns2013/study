from langchain_core.tools import tool
from datetime import datetime
from schemas.tool_schemas import GetCurrentTimeInput, StockHistoryInput
import pytz
import yfinance as yf


# 현재 시각 반환 함수
@tool
def get_current_time(gct_input:GetCurrentTimeInput) -> str:
    """ 현재 시각을 반환하는 함수"""
    tz = pytz.timezone(gct_input.timezone)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    location_and_local_time = f"{gct_input.timezone} ({gct_input.location}) 현재 시각 : {now}"
    return location_and_local_time

# 주식 이력 조회 tool
@tool
def get_yf_stock_history(stock_history_input:StockHistoryInput):
    """ 주식 종목의 가격 데이터를 조회하는 함수 """
    stock = yf.Ticker(stock_history_input.ticker)
    hist = stock.history(stock_history_input.period)
    return str(hist.to_markdown())

# tool 리스트
tools = [get_current_time, get_yf_stock_history]
tool_dict = {
    "get_current_time":get_current_time,
    "get_yf_stock_history":get_yf_stock_history
}
