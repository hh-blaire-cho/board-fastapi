from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.club import Club
    from app.models.member import Member


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # 작성자
    member_id: Mapped[int] = mapped_column(ForeignKey("member.id"), nullable=False)
    member: Mapped["Member"] = relationship(
        "Member",
        back_populates="posts",
    )

    # 소속 클럽
    club_id: Mapped[int] = mapped_column(ForeignKey("club.id"), nullable=False)
    club: Mapped["Club"] = relationship(
        "Club",
        back_populates="posts",
    )

    author_name: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
