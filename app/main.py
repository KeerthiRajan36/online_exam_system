from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.database import engine, Base
from app.routes import (
    auth, students, exams, questions, attempts, results
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Online Examination Management System",
    version="1.0.0",
    description="FastAPI-based Online Exam System"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(students.router)
app.include_router(exams.router)
app.include_router(questions.router)
app.include_router(attempts.router)
app.include_router(results.router)

@app.get("/")
def root():
    return {
        "message": "Online Examination Management System",
        "version": "1.0.0",
        "docs": "/docs"
    }

