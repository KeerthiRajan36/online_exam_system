from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.exam_service import ExamService
from app.schemas.exam import ExamCreate, ExamResponse
from typing import List, Optional

router = APIRouter(prefix="/api/v1/exams", tags=["Exams"])

@router.post("/", response_model=ExamResponse)
def create_exam(
    exam: ExamCreate,
    db: Session = Depends(get_db),
    
):
    try:
        return ExamService.create_exam(db, exam, created_by=1)  
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ExamResponse])
def get_exams(
    category: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return ExamService.get_exams(db, category, page, limit)