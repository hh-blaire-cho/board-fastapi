# app/repositories/club_repository.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.club import Club


# pylint: disable=duplicate-code
class ClubRepository:
    async def save(self, db: AsyncSession, entity: Club) -> Club:
        db.add(entity)
        await db.commit()
        await db.refresh(entity)
        return entity

    async def find_by_id(
        self,
        db: AsyncSession,
        club_id: int,
    ) -> Club | None:
        result = await db.execute(select(Club).where(Club.id == club_id))
        return result.scalar_one_or_none()
