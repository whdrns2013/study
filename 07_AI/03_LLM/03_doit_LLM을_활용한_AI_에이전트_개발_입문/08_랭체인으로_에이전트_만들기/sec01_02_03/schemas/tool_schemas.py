from pydantic import BaseModel, Field

# Schema
class GetCurrentTimeInput(BaseModel):
    timezone: str = Field(..., title="타임존", description="타임존(예: 'Asia/Seoul'). 실제 존재해야 함")
    location: str = Field(..., title="지역명", description="지역명. 타임존은 모든 지명에 대응되지 않으므로 이후 llm 답변 생성에 사용됨")

class StockHistoryInput(BaseModel):
    ticker: str = Field(..., title="주식 코드", description="주식 코드 (예:APPL)"),
    period: str = Field(..., title="기간", description="주식 데이터 조회 기간 (예: 1d, 1mo, 1y)")
