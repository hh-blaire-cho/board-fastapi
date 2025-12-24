# app/models/club.py
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.club_member import ClubMember


class Club(Base):
    __tablename__ = "club"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)

    # 연결 테이블 One To Many
    club_members: Mapped[list[ClubMember]] = relationship(
        "ClubMember", back_populates="club", cascade="all, delete-orphan"
    )
    posts = relationship(
        "Post",
        back_populates="club",
        cascade="all, delete-orphan",
    )
