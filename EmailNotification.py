import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
template_body = """
<!DOCTYPE html>
<html>
<head>
  <title>CircleCI Build Notification</title>
  <style>
    /* Add custom CSS styles here to style your email content */
    body {
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    .header {
      background-color: #008000;
      color: #fff;
      padding: 10px;
      text-align: center;
    }
    .content {
      padding: 20px;
      border: 1px solid #ccc;
    }
    .footer {
	  background-color: #333; 
	  color: #fff; 
	  padding: 1px; 
	  text-align: center; 
	  } 
   </style> 
</head> 
<body> 
	<div class="container">
		<div class="header">
			<h1>CircleCI Job Success</h1>
		</div> 
		<div class="content"> 
			<p>Hello Team</p> 
			<p>Your build in the $CIRCLE_PROJECT_REPONAME repository was $CIRCLE_JOB_NAME.</p>
			<p>Commit: $CIRCLE_SHA1</p> <p>Branch: $CIRCLE_BRANCH</p> <p>Job URL: $CIRCLE_BUILD_URL</p>
			<p>Best regards,</p>
			<p>Your CircleCI bot</p> 
		</div>
		<div class="footer"> 
			<p>This is an automated email from CircleCI. please do not reply.</p>
		</div>
	</div> 
</body>
</html>
"""

notification_message = "Please take action on the following item..."
formatted_body = template_body.format(
    recipient_name="AfridiAltamash",
    sender_name="Ahtesham",
    notification_message=notification_message
)
message = MIMEMultipart()
message.attach(MIMEText(formatted_body, "plain"))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipient, message.as_string())
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")
