# app/models/member.py
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.club_member import ClubMember


class Member(Base):
    __tablename__ = "member"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    # 연결 테이블
    club_members: Mapped[list[ClubMember]] = relationship(
        "ClubMember", back_populates="member", cascade="all, delete-orphan"
    )
