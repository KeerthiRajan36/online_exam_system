from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings
import asyncio

class EmailService:
    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=settings.SMTP_USER,
            MAIL_PASSWORD=settings.SMTP_PASSWORD,
            MAIL_FROM=settings.SMTP_USER,
            MAIL_PORT=settings.SMTP_PORT,
            MAIL_SERVER=settings.SMTP_HOST,
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
        )
        self.fm = FastMail(self.conf)
    
    async def send_email(self, to_email: str, subject: str, body: str):
        message = MessageSchema(
            subject=subject,
            recipients=[to_email],
            body=body,
        )
        await self.fm.send_message(message)

email_service = EmailService()

def send_email_background(to_email: str, subject: str, body: str):
    asyncio.create_task(email_service.send_email(to_email, subject, body))