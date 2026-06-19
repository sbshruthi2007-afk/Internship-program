from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello"}
@app.get("/student/{id}")
def get_student(id):
    return {"student_id": id}
@app.get("/search")
def search(name: str):
    return {"name": name}
class Student(BaseModel):
    name: str
    age: int
@app.post("/student")
def create_student(student: Student):
    return student
@app.put("/student/{id}")
def update_student(id):
    return {"message": f"Student {id} updated"}
@app.delete("/student/{id}")
def delete_student(id):
    return {"message": f"Student {id} deleted"}