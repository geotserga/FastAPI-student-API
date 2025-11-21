from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional
import uvicorn

# STEP 1: Creating the FastAPI application

app = FastAPI(
    title="Student Management API",
    description="API for student management from Excel",
    version="1.0"
)

# Configuring CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# STEP 2: Creating the Excel data

def create_sample_excel():
    data = {
        "ID": [1, 2, 3, 4, 5],
        "Name": ["Giannis Papadopoulos", "Maria Konstantinou", "Petros Anagnostou", "Eleni Dimitriou", "Alexandros Tsaousis"],
        "Department": ["Computer Science", "Computer Science", "Engineering", "Computer Science", "Engineering"],
        "Grade": [8.5, 9.0, 7.5, 8.8, 7.0],
        "Year": [2, 3, 1, 2, 1]
    }
    
    df = pd.DataFrame(data)
    df.to_excel("students.xlsx", index=False, engine="openpyxl")
    print("✓ File students.xlsx created!")
    return df


# STEP 3: Loading data from Excel

def load_students_from_excel(filename="students.xlsx"):
    try:
        df = pd.read_excel(filename, engine="openpyxl")
        return df
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found!")
        print("Creating a new file...")
        return create_sample_excel()
    

# STEP 4: Creating API endpoints

@app.get("/")
def read_root():
    """
    Root page of the API
    """
    return {
        "message": "Welcome to the Student Management API",
        "endpoints": {
            "GET /students": "Get all students",
            "GET /students/{student_id}": "Get a student by ID",
            "GET /students/department/{dept}": "Get students by department",
            "GET /students/top-performers": "Top performing students (grade > 8.5)",
            "POST /students": "Add a new student",
            "DELETE /students/{student_id}": "Delete a student"
        }
    }

@app.get("/students")
def get_all_students():
    """
    Returns all students
    """
    df = load_students_from_excel()
    return {
        "count": len(df),
        "students": df.to_dict(orient="records")
    }

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    """
    Returns a student based on ID
    """
    df = load_students_from_excel()
    student = df[df["ID"] == student_id]
    
    if student.empty:
        return {"error": f"Student with ID {student_id} not found"}, 404
    
    return student.to_dict(orient="records")[0]

@app.get("/students/department/{department}")
def get_students_by_department(department: str):
    """
    Returns students of a specific department
    """
    df = load_students_from_excel()
    students = df[df["Department"] == department]
    
    if students.empty:
        return {"message": f"No students found in the department {department}"}
    
    return {
        "department": department,
        "count": len(students),
        "students": students.to_dict(orient="records")
    }

@app.get("/students/top-performers")
def get_top_performers(min_grade: float = 8.5):
    """
    Returns students with grades above the threshold
    """
    df = load_students_from_excel()
    top_students = df[df["Grade"] >= min_grade].sort_values("Grade", ascending=False)
    
    return {
        "criteria": f"Grade >= {min_grade}",
        "count": len(top_students),
        "students": top_students.to_dict(orient="records")
    }

@app.get("/students/stats")
def get_statistics():
    """
    Returns statistics for students
    """
    df = load_students_from_excel()
    
    return {
        "total_students": len(df),
        "average_grade": round(df["Grade"].mean(), 2),
        "max_grade": float(df["Grade"].max()),
        "min_grade": float(df["Grade"].min()),
        "departments": df["Department"].unique().tolist(),
        "students_by_department": df["Department"].value_counts().to_dict()
    }


# STEP 5: Running the server

if __name__ == "__main__":
    # Create the Excel file if it doesn't exist
    create_sample_excel()
    
    # Run the FastAPI server
    # Open your browser at http://localhost:8000
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=True  # In development mode, automatically reload on changes
    )