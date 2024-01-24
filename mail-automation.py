import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

#Load the environment variables 

current_dir = Path(__file__).resolve().parent if "_file_" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, due_date, invoice_no, amount):
    msg= EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr("Trying out the messenger", f"{send_email}")
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
I hope you are well.
I just wanted to drop you a quick note to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}
I would be really grateful if you could confirm that everything is on track for payment.
Best regards
Khushi Sidana
"""
)
