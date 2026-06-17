from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate
from app.services.auth_service import get_password_hash

class StudentService:
    @staticmethod
    def create_student(db: Session, student_data: StudentCreate):
        
        existing = db.query(Student).filter(Student.email == student_data.email).first()
        if existing:
            raise ValueError("Email already registered")
        
        db_student = Student(
            name=student_data.name,
            email=student_data.email,
            password_hash=get_password_hash(student_data.password)
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    
    @staticmethod
    def get_student_with_exams(db: Session, student_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise ValueError("Student not found")
        return student