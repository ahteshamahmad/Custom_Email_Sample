import smtplib
from email.mime.text import MIMEText

# Set your verified sender email address
sender = "ahtesham.ahmad2018@gmail.com"
# Set your recipient email address
recipient = "altamashfaridi2023@gmail.com"
# Set your SES SMTP server and port
smtp_server = "email-smtp.ap-northeast-1.amazonaws.com"
smtp_port = 587
# Set your SES SMTP credentials
smtp_username = "AKIAZ3KXKBVFZHUIYAU6"
smtp_password = "BLuNCsdn69dLXyQAJYp4vdA3z2PfM79J3zZB0OW2leTW"

# Email content
subject = "CircleCI Build Notification"
body = "Your CircleCI build has completed!"

# Create a MIMEText object
message = MIMEText(body)
message["subject"] = subject
message["From"] = sender
message["To"] = recipient

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipient, message.as_string())
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")
