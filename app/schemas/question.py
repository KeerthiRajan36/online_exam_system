from pydantic import BaseModel, validator
from typing import Optional

class QuestionBase(BaseModel):
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str

class QuestionCreate(QuestionBase):
    exam_id: int
    
    @validator('correct_answer')
    def validate_correct_answer(cls, v):
        if v not in ['A', 'B', 'C', 'D']:
            raise ValueError('Correct answer must be A, B, C, or D')
        return v

class QuestionResponse(QuestionBase):
    id: int
    exam_id: int
    
    class Config:
        from_attributes = True