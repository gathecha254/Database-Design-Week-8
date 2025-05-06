from pydantic import BaseModel
from typing import Optional

# Schema for creating a member
class MemberCreate(BaseModel):
    name: str
    email: str

# Schema for responding with member data
class Member(MemberCreate):
    id: int

    class Config:
        orm_mode = True
