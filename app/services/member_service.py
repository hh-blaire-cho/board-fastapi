# app/services/member_service.py

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dto.member_dto import MemberDto
from app.dto.member_request import MemberCreateRequest
from app.models.member import Member
from app.repositories.member_repository import MemberRepository

member_repo = MemberRepository()


class MemberService:
    async def create_member(
        self, db: AsyncSession, req: MemberCreateRequest
    ) -> MemberDto:
        member = Member(
            first_name=req.first_name,
            last_name=req.last_name,
            email=req.email,
        )
        saved_member = await member_repo.save(db, member)
        return MemberDto.model_validate(saved_member)

    async def get_member(self, db: AsyncSession, member_id: int) -> MemberDto:
        member = await member_repo.find_by_id(db, member_id)
        if member is None:
            raise HTTPException(status_code=404, detail="Member not found")

        return MemberDto.model_validate(member)
