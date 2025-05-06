from pydantic import BaseModel
from typing import Optional

# Base model for Member
class MemberBase(BaseModel):
    name: str
    email: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True


# Base model for Author
class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    nationality: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


# Base model for Category
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# Base model for Book
class BookBase(BaseModel):
    title: str
    isbn: str
    published_year: Optional[int] = None
    category_id: Optional[int] = None
    quantity_available: int = 1

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
