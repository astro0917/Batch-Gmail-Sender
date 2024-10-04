import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "your_email@example.com"
password = "your_secure_app_password"

recipients = [
    
    {"email": "recipients_email", "name": "recipients_name"},
    
      
]

subject = "your subject title goes here"
email_template = """

YOUR HTML BODY OF TEXT GOES HERE

"""
def send_email(to_email, name):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    
    server.login(sender_email,password)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    body = email_template.format(name=name)
    msg.attach(MIMEText(body, 'html'))
    
    server.sendmail(sender_email, to_email, msg.as_string())
    server.quit()
    
for recipient in recipients:
    send_email(recipient['email'], recipient['name'])
    print(f"Email succesfully sent to {recipient['name']} at {recipient['email']}")
