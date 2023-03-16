from enum import Enum
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Student(BaseModel):
    id : str
    name : str
    clase : int


app = FastAPI()

students = []

@app.get("/")
async def mensaje():
    return {"Hello":"World"}


@app.get("/login")
async def missage():
    return "Ingrese sus datos"


@app.get("/users/{user_id}")
async def mensaje(user_id: int):
    return f"El id del usuario es: {user_id}"

@app.get("/students")
async def get_students(): 
    return students

@app.get("/student/{id}")
def get_student(id: str):
    for student in students: 
        if student["id"] ==id: 
            return student
    return "No se ha encontrado estudiante"

@app.post("/students")
async def save_student(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return "Estudiante registrado"

@app.put("/students/{id}")
def update_student(updated_student: Student, id:str): 
    for student in students: 
        if student["id"] ==id: 
            student["name"] = updated_student.name
            student["clase"] = updated_student.clase
            return "Estudiante modificado"
    return "No existe estudiante"

@app.delete("/students/")
def delete_student(id: str): 
    for student in students: 
        if student["id"] == id: 
            students.remove(student)
            return "Estudiante eliminado"
    return "No existe el estudiante"


