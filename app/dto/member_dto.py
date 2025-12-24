from pydantic import BaseModel, EmailStr


class MemberDto(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True
