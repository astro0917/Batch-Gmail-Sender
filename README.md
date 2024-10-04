This project is a Python script that allows you to send personalized batch emails to multiple recipients. The script automates the process of sending an email to a list of recipients, while customizing each email with the recipient's name and a personalized message.

Features:
Send batch emails to multiple recipients.
Personalize each email with the recipient's name.
HTML email templates are supported, allowing for formatted content and hyperlinks.
Easily configurable using environment variables for security.
Prerequisites:
Before you can run the script, ensure you have the following set up:

Python 3.6+: This project uses Python for scripting.
Gmail Account: The script uses Gmail's SMTP server to send emails. You must enable App Passwords for your Gmail account or enable "Less secure apps" (not recommended).
Getting Started
1. Clone the Repository
To get started, clone this repository to your local machine:

bash
Copy code
git clone https://github.com/astro0917/Batch-Gmail-Sender.git
cd Batch-Gmail-Sender
2. Install Dependencies
This project uses the python-dotenv library to manage environment variables. Install it with pip:

bash
Copy code
pip install python-dotenv
3. Create a .env File
In the root directory of the project, create a .env file where you will store your Gmail credentials (email and app-specific password). This file will not be tracked by Git, so your credentials are safe.

Create the .env file:

bash
Copy code
touch .env
Inside the .env file, add your Gmail email address and password:

bash
Copy code
# .env file

SENDER_EMAIL=your_email@gmail.com
PASSWORD=your_app_password
4. Edit the Email Template
You can customize the email content by editing the HTML template in the script. Open the gMAIL.py file and adjust the email body according to your needs.

For example:

html
Copy code
email_template = """
<html>
  <body>
    <p>Hi {name}!</p>
    <p>I hope this message brings a smile to your face! 😊</p>
    <p>We’re beyond excited to introduce our latest small jewelry collection at Chvker, and we think you would be the perfect fit to help us share it with the world! 💎✨</p>
    <p>If you’re interested, simply fill out <a href="https://www.example.com">this form</a> to get started, and we’ll be in touch soon! 🌟</p>
    <p>Warmest wishes,<br>Monica<br>Team Chvker Jewelry 💌✨</p>
  </body>
</html>
"""
The {name} placeholder will be replaced by each recipient's name.

5. Add Recipients
You can add a list of recipients (name and email) in the script like this:

python
Copy code
recipients = [
    {"email": "example1@example.com", "name": "Brooke"},
    {"email": "example2@example.com", "name": "Alice"},
    {"email": "example3@example.com", "name": "Sophia"}
]
Each email will be personalized with the name of the recipient.

6. Run the Script
Now that everything is set up, you can run the script to send emails. Ensure you're in the project directory, then run:

bash
Copy code
python gMAIL.py
If everything is configured correctly, the script will start sending emails to your recipients.
