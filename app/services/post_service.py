# app/services/post_service.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.post_dto import PostDto
from app.dto.post_request import PostCreateRequest
from app.models.post import Post
from app.repositories.member_repository import MemberRepository
from app.repositories.post_repository import PostRepository

post_repo = PostRepository()
member_repo = MemberRepository()


class PostService:
    async def create_post(self, db: AsyncSession, req: PostCreateRequest) -> PostDto:
        member = await member_repo.find_by_id(db, req.member_id)
        if member is None:
            raise HTTPException(status_code=404, detail="Member not found")

        post = Post(
            member_id=req.member_id,
            author_name=req.author_name,
            content=req.content,
        )

        post = await post_repo.save(db, post)
        return PostDto.model_validate(post)

    async def get_post(self, db: AsyncSession, post_id: int) -> PostDto:
        post = await post_repo.find_by_id(db, post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")

        return PostDto.model_validate(post)
