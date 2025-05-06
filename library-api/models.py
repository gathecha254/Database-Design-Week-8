from pydantic import BaseModel
from typing import Optional

# Base model for Member
class MemberBase(BaseModel):
    name: str
    email: str

# Model for creating a member
class MemberCreate(MemberBase):
    pass

# Model for reading a member (includes ID)
class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True
