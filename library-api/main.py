from fastapi import FastAPI, Depends, HTTPException
from typing import List
import database
from models import Member, MemberCreate

app = FastAPI()

# GET all members
@app.get("/members", response_model=List[Member])
def read_members():
    db = database.get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

# CREATE a new member
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

# GET a single member by ID
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

# UPDATE an existing member
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

# DELETE a member
@app.delete("/members/{member_id}")
def delete_member(member_id: int):
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Members WHERE MemberID = %s", (member_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Member deleted"}
