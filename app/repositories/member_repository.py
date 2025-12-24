# app/repositories/member_repository.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.member import Member


# pylint: disable=duplicate-code
class MemberRepository:
    async def save(self, db: AsyncSession, entity: Member) -> Member:
        db.add(entity)
        await db.commit()
        await db.refresh(entity)
        return entity

    async def find_by_id(
        self,
        db: AsyncSession,
        member_id: int,
    ) -> Member | None:
        result = await db.execute(select(Member).where(Member.id == member_id))
        return result.scalar_one_or_none()
