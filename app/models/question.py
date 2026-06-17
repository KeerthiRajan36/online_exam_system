from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_answer = Column(String(1), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    
    exam = relationship("Exam", back_populates="questions")