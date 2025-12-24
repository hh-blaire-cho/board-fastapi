# app/dto/post_request.py
from pydantic import BaseModel, Field


class PostCreateRequest(BaseModel):
    author_name: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    member_id: int
