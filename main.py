from fastapi import FastAPI, HTTPException, status, Query
from bson import ObjectId
from models import Student, Address
from database import collection

app = FastAPI()

@app.post("/students/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    inserted = collection.insert_one(student.dict(by_alias=True))
    return {"id": str(inserted.inserted_id)}

@app.get("/students/", response_model=list[Student])
def list_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}
    students = collection.find(query)
    return [Student(**{**student, "id": str(student["_id"])}) for student in students]

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: str):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student:
        student["id"] = str(student.pop("_id"))
        return student
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

@app.patch("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_student(student_id: str, student: Student):
    updated = collection.update_one({"_id": ObjectId(student_id)}, {"$set": student.dict(exclude_unset=True)})
    if updated.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: str):
    deleted = collection.delete_one({"_id": ObjectId(student_id)})
    if deleted.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")


