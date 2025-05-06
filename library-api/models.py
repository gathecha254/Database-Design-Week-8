from pydantic import BaseModel
from typing import Optional

# Member
class MemberBase(BaseModel):
    name: str
    email: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True


# Author
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


# Category
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# Book
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


# Loan
class LoanBase(BaseModel):
    member_id: int
    book_id: int
    due_date: str

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    loan_date: str
    return_date: Optional[str]

    class Config:
        orm_mode = True


# Reservation
class ReservationBase(BaseModel):
    member_id: int
    book_id: int

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int
    reservation_date: str
    status: str

    class Config:
        orm_mode = True
