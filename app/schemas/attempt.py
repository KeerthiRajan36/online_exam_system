from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AttemptStart(BaseModel):
    student_id: int
    exam_id: int

class AttemptSubmit(BaseModel):
    attempt_id: int
    answers: dict  # question_id: selected_option

class AttemptResponse(BaseModel):
    id: int
    student_id: int
    exam_id: int
    score: Optional[float]
    status: str
    started_at: datetime
    completed_at: Optional[datetime]
    
    class Config:
        from_attributes = True