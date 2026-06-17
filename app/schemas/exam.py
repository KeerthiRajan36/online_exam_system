from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ExamBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: str
    duration_minutes: int

class ExamCreate(ExamBase):
    pass

class ExamResponse(ExamBase):
    id: int
    is_active: bool
    created_at: datetime
    created_by: int
    
    class Config:
        from_attributes = True