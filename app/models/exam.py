from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Exam(Base):
    __tablename__ = "exams"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String, index=True)
    duration_minutes = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, ForeignKey("students.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    questions = relationship("Question", back_populates="exam", cascade="all, delete-orphan")
    attempts = relationship("Attempt", back_populates="exam")
    creator = relationship("Student", foreign_keys=[created_by])