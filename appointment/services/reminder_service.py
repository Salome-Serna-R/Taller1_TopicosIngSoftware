from .email_interface import EmailService

class ReminderService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service  # Inyección de dependencia

    def send_reminder(self, reminder):
        subject = f"WeCare Reminder: {reminder.reminder_title}"
        message = reminder.reminder_message
        self.email_service.send_email(reminder.reminder_email, subject, message)
