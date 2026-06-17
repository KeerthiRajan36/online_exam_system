from sqlalchemy.orm import Session
from app.models.attempt import Attempt
from app.models.student import Student

class ResultService:
    @staticmethod
    def get_results(db: Session, student_id: int = None, page: int = 1, limit: int = 10):
        query = db.query(Attempt).filter(Attempt.status == "Completed")
        if student_id:
            query = query.filter(Attempt.student_id == student_id)
        return query.offset((page - 1) * limit).limit(limit).all()
    
    @staticmethod
    def get_leaderboard(db: Session, limit: int = 10):
        return db.query(
            Student,
            Attempt.score
        ).join(
            Attempt, Student.id == Attempt.student_id
        ).filter(
            Attempt.status == "Completed"
        ).order_by(
            Attempt.score.desc()
        ).limit(limit).all()