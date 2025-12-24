# app/models/post.py
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    member_id: Mapped[int] = mapped_column(ForeignKey("member.id"), nullable=False)
    member = relationship("Member")

    club_id: Mapped[int] = mapped_column(ForeignKey("club.id"), nullable=False)
    club = relationship("Club")

    author_name: Mapped[str] = mapped_column(String(255), nullable=False)

    content: Mapped[str] = mapped_column(Text, nullable=False)
