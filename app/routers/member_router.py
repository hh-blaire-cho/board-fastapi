# app/routers/member_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.dto.member_dto import MemberDto
from app.dto.member_request import MemberCreateRequest
from app.services.member_service import MemberService

router = APIRouter(prefix="/v1/members", tags=["Members"])
service = MemberService()


@router.post("/", response_model=MemberDto)
async def create_member_api(
    req: MemberCreateRequest, db: AsyncSession = Depends(get_db)
):
    return await service.create_member(db, req)


@router.get("/{member_id}", response_model=MemberDto)
async def get_member_api(member_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_member(db, member_id)
