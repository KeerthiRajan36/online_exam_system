from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.result_service import ResultService
from app.schemas.attempt import AttemptResponse
from typing import List, Optional

router = APIRouter(prefix="/api/v1/results", tags=["Results"])

@router.get("/", response_model=List[AttemptResponse])
def get_results(
    student_id: Optional[int] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return ResultService.get_results(db, student_id, page, limit)

@router.get("/leaderboard")
def get_leaderboard(limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db)):
    return ResultService.get_leaderboard(db, limit)