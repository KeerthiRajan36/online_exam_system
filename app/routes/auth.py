from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import authenticate_student, create_access_token
from app.schemas.auth import LoginRequest, Token

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    student = authenticate_student(db, request.email, request.password)
    if not student:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": str(student.id), "role": "student"}
    )
    return {"access_token": access_token, "token_type": "bearer"}