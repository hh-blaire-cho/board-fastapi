# app/repositories/post_repository.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.post import Post


# pylint: disable=duplicate-code
class PostRepository:
    async def save(self, db: AsyncSession, entity: Post) -> Post:
        db.add(entity)
        await db.commit()
        await db.refresh(entity)
        return entity

    async def find_by_id(
        self,
        db: AsyncSession,
        post_id: int,
    ) -> Post | None:
        result = await db.execute(select(Post).where(Post.id == post_id))
        return result.scalar_one_or_none()
