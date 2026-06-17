from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    password_hash = Column(String,default=True)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.utcnow())

    attempts = relationship("Attempt", back_populates="student")

    