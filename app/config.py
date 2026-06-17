from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./exam_system.db"
    SECRET_KEY: str = "EXAM_SECRET_KEY"
    ALGORITHM: str = "HS256"  
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    
    class Config:
        env_file = ".env"
        extra = "ignore"  

settings = Settings()