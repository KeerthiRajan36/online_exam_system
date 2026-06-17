from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    password: str

class StudentResponse(StudentBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True