from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.question_service import QuestionService
from app.schemas.question import QuestionCreate, QuestionResponse
from typing import List

router = APIRouter(prefix="/api/v1/questions", tags=["Questions"])

@router.post("/", response_model=QuestionResponse)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    try:
        return QuestionService.create_question(db, question)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/exams/{exam_id}/questions", response_model=List[QuestionResponse])
def get_exam_questions(exam_id: int, db: Session = Depends(get_db)):
    try:
        return QuestionService.get_exam_questions(db, exam_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))