from pydantic import BaseModel, EmailStr


class MemberCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
