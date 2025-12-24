# app/dto/post_request.py
from pydantic import BaseModel, Field


class PostCreateRequest(BaseModel):
    content: str = Field(..., min_length=1)
    member_id: int
    club_id: int
