from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

students = {
    "S001": {"name": "Ravi" , "marks": 85, "grade": "A"},
    "S002": {"name": "Priya" , "marks": 72, "grade": "B"},
    "S003": {"name": "Arjun" , "marks": 91, "grade": "A+"}   
}
#input schema     
class MarksSubmission(BaseModel):
    student_id : str
    marks : int
    subject : str

@app.get("/student/{student_id}")
def get_student(student_id: str):

    if student_id not in students:
        raise HTTPException(
        status_code = 404,
        detail = f"student with  ID {student_id} does not exists"
    )
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission: MarksSubmission):

    #error 1 students does not exits
    if submission.student_id not in students:
        raise HTTPException(
            status_code = 404,
            detail =  f"student with ID {submission.student_id} does not exists"
        )
    
    #error2 valid range 0 - 120
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(
            status_code = 400,
            detail = {
                "error": "marks must be between 0 and 100",
                "marks_recieved": submission.marks, 
                "fix":"enter a valid value between 0 and 200"
            }
        )
    #error3 subject name empty
    if submission.subject.strip() == "":
        raise HTTPException(
            status_code =  400,
            detail = "subject name cannot be empty"
        )

    try:
        students[submission.student_id]["marks"] = submission.marks

        return {
            "message" : "marks submitted successfully",
            "student" : students[submission.student_id]["name"],
            "subject" : submission.subjects,
            "marks": submission.marks
        }
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"Something went wrong from our side {str(e)}"
        )
#there is 3 layer of exception handeling 
#1. pydantic , 2. HTTPExeption , 3. try catch