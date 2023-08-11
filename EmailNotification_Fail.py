import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

circle_project_reponame = os.environ.get("CIRCLE_PROJECT_REPONAME")
circle_project_username = os.environ.get("CIRCLE_PROJECT_USERNAME")
circle_repository_url = os.environ.get("CIRCLE_REPOSITORY_URL")
circle_branchname = os.environ.get("CIRCLE_BRANCH")
circle_sha1 = os.environ.get("CIRCLE_SHA1")
circle_workflow_id = os.environ.get("CIRCLE_WORKFLOW_ID")

print(circle_project_reponame)
print(circle_project_username)
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
      background-color: #FF0000;
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
			<h1>CircleCI Job Failed</h1>
		</div> 
		<div class="content"> 
			<p>Hello Team</p> 
			<p>Your build in the {circle_project_reponame} </p>
			<p>User {circle_project_username} </p>
			<p>Commit: {circle_sha1} </p>
			<p>Branch: {circle_branchname} </p>
			<p>Job URL: {circle_repository_url} </p>
			<p>Workflow Id: {circle_workflow_id} </p>
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

message = MIMEMultipart()
message.attach(MIMEText(template_body, "html"))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipient, message.as_string())
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")
