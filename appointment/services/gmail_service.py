import smtplib
from .email_interface import EmailService

class GmailService(EmailService):
    def send_email(self, to_email, subject, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("tu_correo@gmail.com", "tu_password")  # ⚠️ usar variables de entorno
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail("tu_correo@gmail.com", to_email, email_message)
        server.quit()
