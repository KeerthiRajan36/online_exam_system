from sqlalchemy.orm import Session
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.exam import ExamCreate

class ExamService:
    @staticmethod
    def create_exam(db: Session, exam_data: ExamCreate, created_by: int):
        if exam_data.duration_minutes <= 0:
            raise ValueError("Exam duration must be greater than 0")
            
        db_exam = Exam(
            title=exam_data.title,
            description=exam_data.description,
            category=exam_data.category,
            duration_minutes=exam_data.duration_minutes,
            created_by=created_by
        )
        db.add(db_exam)
        db.commit()
        db.refresh(db_exam)
        return db_exam
    
    @staticmethod
    def get_exams(db: Session, category: str = None, page: int = 1, limit: int = 10):
        query = db.query(Exam)
        if category:
            query = query.filter(Exam.category == category)
        return query.offset((page - 1) * limit).limit(limit).all()