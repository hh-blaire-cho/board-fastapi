# app/routers/post_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.dto.post_dto import PostDto
from app.dto.post_request import PostCreateRequest
from app.services.post_service import PostService

router = APIRouter(prefix="/v1/posts", tags=["Posts"])
service = PostService()


@router.post("/", response_model=PostDto)
async def create_post_api(req: PostCreateRequest, db: AsyncSession = Depends(get_db)):
    return await service.create_post(db, req)


@router.get("/{member_id}", response_model=PostDto)
async def get_member_api(post_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_post(db, post_id)
