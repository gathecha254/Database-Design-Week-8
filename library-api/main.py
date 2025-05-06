from fastapi import FastAPI, Depends, HTTPException
from typing import List
import database
from models import Member, MemberCreate, Author, AuthorCreate, Category, CategoryCreate, Book, BookCreate

app = FastAPI()

# ===== MEMBER ENDPOINTS =====
@app.get("/members", response_model=List[Member])
def read_members():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

@app.post("/members", response_model=Member)
def create_member(member: MemberCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = "INSERT INTO Members (Name, Email) VALUES (%s, %s)"
    values = (member.name, member.email)
    cursor.execute(query, values)
    db.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (new_id,))
    new_member = cursor.fetchone()
    cursor.close()
    db.close()
    return {**member.dict(), "id": new_id}

@app.get("/members/{member_id}", response_model=Member)
def read_member(member_id: int):
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (member_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Member not found")
    return result

@app.put("/members/{member_id}")
def update_member(member_id: int, member: MemberCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = "UPDATE Members SET Name = %s, Email = %s WHERE MemberID = %s"
    values = (member.name, member.email, member_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Member updated"}

@app.delete("/members/{member_id}")
def delete_member(member_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Members WHERE MemberID = %s", (member_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Member deleted"}


# ===== AUTHOR ENDPOINTS =====
@app.get("/authors", response_model=List[Author])
def read_authors():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Authors")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

@app.post("/authors", response_model=Author)
def create_author(author: AuthorCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = "INSERT INTO Authors (FirstName, LastName, Nationality) VALUES (%s, %s, %s)"
    values = (author.first_name, author.last_name, author.nationality)
    cursor.execute(query, values)
    db.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Authors WHERE AuthorID = %s", (new_id,))
    new_author = cursor.fetchone()
    cursor.close()
    db.close()
    return {**author.dict(), "id": new_id}

@app.get("/authors/{author_id}", response_model=Author)
def read_author(author_id: int):
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Authors WHERE AuthorID = %s", (author_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Author not found")
    return result

@app.put("/authors/{author_id}")
def update_author(author_id: int, author: AuthorCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = "UPDATE Authors SET FirstName = %s, LastName = %s, Nationality = %s WHERE AuthorID = %s"
    values = (author.first_name, author.last_name, author.nationality, author_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Author updated"}

@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Authors WHERE AuthorID = %s", (author_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Author deleted"}


# ===== CATEGORY ENDPOINTS =====
@app.get("/categories", response_model=List[Category])
def read_categories():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Categories")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

@app.post("/categories", response_model=Category)
def create_category(category: CategoryCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = "INSERT INTO Categories (CategoryName) VALUES (%s)"
    values = (category.name,)
    cursor.execute(query, values)
    db.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Categories WHERE CategoryID = %s", (new_id,))
    new_category = cursor.fetchone()
    cursor.close()
    db.close()
    return {**category.dict(), "id": new_id}

@app.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int):
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Categories WHERE CategoryID = %s", (category_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return result

@app.put("/categories/{category_id}")
def update_category(category_id: int, category: CategoryCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = "UPDATE Categories SET CategoryName = %s WHERE CategoryID = %s"
    values = (category.name, category_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Category updated"}

@app.delete("/categories/{category_id}")
def delete_category(category_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Categories WHERE CategoryID = %s", (category_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Category deleted"}


# ===== BOOK ENDPOINTS =====
@app.get("/books", response_model=List[Book])
def read_books():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Books")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

@app.post("/books", response_model=Book)
def create_book(book: BookCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO Books (Title, ISBN, PublishedYear, CategoryID, QuantityAvailable)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        book.title,
        book.isbn,
        book.published_year,
        book.category_id,
        book.quantity_available
    )
    cursor.execute(query, values)
    db.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Books WHERE BookID = %s", (new_id,))
    new_book = cursor.fetchone()
    cursor.close()
    db.close()
    return {**book.dict(), "id": new_id}

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Books WHERE BookID = %s", (book_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return result

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = """
    UPDATE Books SET 
      Title = %s, 
      ISBN = %s, 
      PublishedYear = %s, 
      CategoryID = %s, 
      QuantityAvailable = %s 
    WHERE BookID = %s
    """
    values = (
        book.title,
        book.isbn,
        book.published_year,
        book.category_id,
        book.quantity_available,
        book_id
    )
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Book updated"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Books WHERE BookID = %s", (book_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Book deleted"}


# ===== LOAN ENDPOINTS =====
@app.get("/loans", response_model=List[Loan])
def read_loans():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Loans")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

@app.post("/loans", response_model=Loan)
def create_loan(loan: LoanCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO Loans (MemberID, BookID, DueDate) VALUES (%s, %s, %s)
    """
    values = (loan.member_id, loan.book_id, loan.due_date)
    cursor.execute(query, values)
    db.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Loans WHERE LoanID = %s", (new_id,))
    new_loan = cursor.fetchone()
    cursor.close()
    db.close()
    return {**loan.dict(), "id": new_id, "loan_date": new_loan['LoanDate'], "return_date": new_loan['ReturnDate']}

@app.get("/loans/{loan_id}", response_model=Loan)
def read_loan(loan_id: int):
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Loans WHERE LoanID = %s", (loan_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Loan not found")
    return result

@app.put("/loans/{loan_id}")
def update_loan(loan_id: int, loan: LoanCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = """
    UPDATE Loans SET 
      MemberID = %s,
      BookID = %s,
      DueDate = %s
    WHERE LoanID = %s
    """
    values = (loan.member_id, loan.book_id, loan.due_date, loan_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Loan updated"}

@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Loans WHERE LoanID = %s", (loan_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Loan deleted"}


# ===== RESERVATION ENDPOINTS =====
@app.get("/reservations", response_model=List[Reservation])
def read_reservations():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Reservations")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

@app.post("/reservations", response_model=Reservation)
def create_reservation(reservation: ReservationCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO Reservations (MemberID, BookID) VALUES (%s, %s)
    """
    values = (reservation.member_id, reservation.book_id)
    cursor.execute(query, values)
    db.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Reservations WHERE ReservationID = %s", (new_id,))
    new_reservation = cursor.fetchone()
    cursor.close()
    db.close()
    return {
        **reservation.dict(),
        "id": new_id,
        "reservation_date": new_reservation['ReservationDate'],
        "status": new_reservation['Status']
    }

@app.get("/reservations/{reservation_id}", response_model=Reservation)
def read_reservation(reservation_id: int):
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Reservations WHERE ReservationID = %s", (reservation_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return result

@app.put("/reservations/{reservation_id}")
def update_reservation(reservation_id: int, reservation: ReservationCreate):
    db = database.get_db()
    cursor = db.cursor()
    query = """
    UPDATE Reservations SET 
      MemberID = %s,
      BookID = %s
    WHERE ReservationID = %s
    """
    values = (reservation.member_id, reservation.book_id, reservation_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Reservation updated"}

@app.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Reservations WHERE ReservationID = %s", (reservation_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Reservation deleted"}
