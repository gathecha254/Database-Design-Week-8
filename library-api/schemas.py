from pydantic import BaseModel
from typing import Optional

# Schemas for Member
class MemberCreate(BaseModel):
    name: str
    email: str

class Member(MemberCreate):
    id: int

    class Config:
        orm_mode = True


# Schemas for Author
class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    nationality: Optional[str]

class Author(AuthorCreate):
    id: int

    class Config:
        orm_mode = True


# Schemas for Category
class CategoryCreate(BaseModel):
    name: str

class Category(CategoryCreate):
    id: int

    class Config:
        orm_mode = True


# Schemas for Book
class BookCreate(BaseModel):
    title: str
    isbn: str
    published_year: Optional[int]
    category_id: Optional[int]
    quantity_available: int = 1

class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True


# Schemas for Loan
class LoanCreate(BaseModel):
    member_id: int
    book_id: int
    due_date: str

class Loan(LoanCreate):
    id: int
    loan_date: str
    return_date: Optional[str]

    class Config:
        orm_mode = True


# Schemas for Reservation
class ReservationCreate(BaseModel):
    member_id: int
    book_id: int

class Reservation(ReservationCreate):
    id: int
    reservation_date: str
    status: str

    class Config:
        orm_mode = True
