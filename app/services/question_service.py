from sqlalchemy.orm import Session
from app.models.question import Question
from app.models.exam import Exam
from app.schemas.question import QuestionCreate

class QuestionService:
    @staticmethod
    def create_question(db: Session, question_data: QuestionCreate):
        
        exam = db.query(Exam).filter(Exam.id == question_data.exam_id).first()
        if not exam or not exam.is_active:
            raise ValueError("Exam not found or inactive")
        
        
        existing_questions = db.query(Question).filter(Question.exam_id == question_data.exam_id).count()
        if existing_questions >= 5:
            raise ValueError("Exam already has minimum 5 questions")
        
        db_question = Question(**question_data.dict())
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question
    
    @staticmethod
    def get_exam_questions(db: Session, exam_id: int):
        exam = db.query(Exam).filter(Exam.id == exam_id).first()
        if not exam:
            raise ValueError("Exam not found")
        return exam.questions