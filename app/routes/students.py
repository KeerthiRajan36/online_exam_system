from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.student_service import StudentService
from app.services.exam_service import ExamService
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.exam import ExamResponse
from typing import List

router = APIRouter(prefix="/api/v1/students", tags=["Students"])

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        return StudentService.create_student(db, student)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{student_id}/exams", response_model=List[ExamResponse])
def get_student_exams(student_id: int, db: Session = Depends(get_db)):
    student = StudentService.get_student_with_exams(db, student_id)
    
    return []