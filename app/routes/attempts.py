from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.attempt_service import AttemptService
from app.schemas.attempt import AttemptStart, AttemptSubmit, AttemptResponse
from typing import List, Optional

router = APIRouter(prefix="/api/v1/attempts", tags=["Attempts"])

@router.post("/start", response_model=AttemptResponse)
def start_attempt(attempt: AttemptStart, db: Session = Depends(get_db)):
    try:
        return AttemptService.start_attempt(db, attempt.student_id, attempt.exam_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/submit", response_model=AttemptResponse)
def submit_attempt(submission: AttemptSubmit, db: Session = Depends(get_db)):
    try:
        return AttemptService.submit_attempt(db, submission.attempt_id, submission.answers)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{attempt_id}", response_model=AttemptResponse)
def get_attempt(attempt_id: int, db: Session = Depends(get_db)):
    attempt = AttemptService.get_attempt(db, attempt_id)
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")
    return attempt

@router.get("/", response_model=List[AttemptResponse])
def get_attempts(
    status: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return AttemptService.get_attempts_by_status(db, status, page, limit)