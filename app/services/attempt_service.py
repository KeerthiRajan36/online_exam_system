from sqlalchemy.orm import Session
from app.models.attempt import Attempt
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.attempt import AttemptSubmit
from app.utils.email import EmailService
from datetime import datetime

class AttemptService:
    @staticmethod
    def start_attempt(db: Session, student_id: int, exam_id: int):
        
        existing = db.query(Attempt).filter(
            Attempt.student_id == student_id,
            Attempt.exam_id == exam_id
        ).first()
        if existing:
            raise ValueError("Student already attempted this exam")
        
        
        exam = db.query(Exam).filter(Exam.id == exam_id).first()
        if not exam or not exam.is_active:
            raise ValueError("Exam not found or inactive")
        
        attempt = Attempt(
            student_id=student_id,
            exam_id=exam_id,
            status="Started"
        )
        db.add(attempt)
        db.commit()
        db.refresh(attempt)
        return attempt
    
    @staticmethod
    def submit_attempt(db: Session, attempt_id: int, answers: dict):
        attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
        if not attempt:
            raise ValueError("Attempt not found")
        
        if attempt.status == "Completed":
            raise ValueError("Attempt already completed")
        
        
        questions = db.query(Question).filter(Question.exam_id == attempt.exam_id).all()
        correct_answers = 0
        total_questions = len(questions)
        
        for question in questions:
            if str(question.id) in answers:
                if answers[str(question.id)] == question.correct_answer:
                    correct_answers += 1
        
        score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        
        attempt.score = score
        attempt.status = "Completed"
        attempt.completed_at = datetime.utcnow()
        
        db.commit()
        db.refresh(attempt)
        
        
        student = attempt.student
        EmailService.send_email.delay(
            to_email=student.email,
            subject="Exam Completed",
            body=f"Your score for {attempt.exam.title}: {score:.2f}%"
        )
        
        return attempt
    
    @staticmethod
    def get_attempt(db: Session, attempt_id: int):
        return db.query(Attempt).filter(Attempt.id == attempt_id).first()
    
    @staticmethod
    def get_attempts_by_status(db: Session, status: str = None, page: int = 1, limit: int = 10):
        query = db.query(Attempt)
        if status:
            query = query.filter(Attempt.status == status)
        return query.offset((page - 1) * limit).limit(limit).all()