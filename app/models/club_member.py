# app/models/club_member.py
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.club import Club
    from app.models.member import Member


class ClubMember(Base):
    __tablename__ = "club_member"

    club_id: Mapped[int] = mapped_column(ForeignKey("club.id"), primary_key=True)
    member_id: Mapped[int] = mapped_column(ForeignKey("member.id"), primary_key=True)

    club: Mapped["Club"] = relationship("Club", back_populates="club_members")
    member: Mapped["Member"] = relationship("Member", back_populates="club_members")

    owner: Mapped[bool] = mapped_column(Boolean, default=False)
    approved_at: Mapped[str] = mapped_column(nullable=True)  # datetime 필드 가능
