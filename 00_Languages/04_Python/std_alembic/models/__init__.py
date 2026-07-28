from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id    : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="사용자 고유 번호")
    name  : Mapped[str] = mapped_column(String(50), index=True, comment="사용자 이름")
    email : Mapped[str] = mapped_column(String(100), comment="사용자 이메일")
    age   : Mapped[int] = mapped_column(Integer, comment="사용자 나이", nullable=True)

class Plant(Base):
    __tablename__ = "plants"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment="식물의 고유 번호")
    name: Mapped[str] = mapped_column(String(50), comment="식물의 이름")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), comment="소유 사용자 고유 번호")
    
from models.activity import Activity