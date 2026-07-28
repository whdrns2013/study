from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey

class Activity(Base):
    __tablename__ = "activities"
    
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="관리활동 ID")
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"), comment="관리활동 사용자 ID")
    plant_id : Mapped[int] = mapped_column(ForeignKey("plants.id"), comment="관리활동 식물 ID")
    activity_type : Mapped[str] = mapped_column(String(10), comment="관리활동 유형")
    activity_content : Mapped[str] = mapped_column(String(2000), comment="관리활동 내용")