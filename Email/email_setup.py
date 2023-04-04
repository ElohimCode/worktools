import smtplib, ssl
from email.message import EmailMessage
from ..secret import sender_email_address, sender_password

def send_email_gmail(email, name=None):
    # SMTP Configuration for gmail server
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    # sender login details
    sender_email, password = sender_email_address, sender_password   

    msg = EmailMessage()
    msg.set_content(f"Hi {name}, \nI hope you're doing fine. \nI'm Just testing my scripts")
    msg['Subject'] = "Testing"
    msg['From'] = sender_email
    msg['To'] = email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email, to_addrs=email)
    except Exception as err:
        print(f"An errror has occured, {err}")
