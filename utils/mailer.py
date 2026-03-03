from flask_mail import Mail, Message
from flask import current_app

def send_confirmation_mail(name, email, event):
    mail = Mail(current_app)
    msg = Message(
        subject=f"Voyage Confirmed: {event} - Odyssey of the Unbound",
        recipients=[email],
        body=f"Ahoy {name},\n\nYour registration for {event} is confirmed!\nPrepare to embark on an unbound journey of innovation.\n\n— Team Empulse 2026"
    )
    mail.send(msg)
