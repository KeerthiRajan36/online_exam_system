from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Attempt(Base):
    __tablename__ = "attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    score = Column(Float)
    status = Column(String, default="Started") 
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)
    
    student = relationship("Student", back_populates="attempts")
    exam = relationship("Exam", back_populates="attempts")