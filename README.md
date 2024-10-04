# Personalized Batch Gmail Sender

This project is a Python script that allows you to send personalized batch emails to multiple recipients. The script automates the process of sending an email to a list of recipients, while customizing each email with the recipient's name and a personalized message.

Features:
Send batch emails to multiple recipients.
Personalize each email with the recipient's name.
HTML email templates are supported, allowing for formatted content and hyperlinks.
Easily configurable using environment variables for security.

Before you can run the script, ensure you have the following set up:

Gmail Account: The script uses Gmail's SMTP server to send emails. You **must** enable [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) for your Gmail account.

## Getting Started

### Clone the Repository
   
To get started, clone this repository to your local machine:
```
git clone https://github.com/astro0917/Batch-Gmail-Sender.git
cd Batch-Gmail-Sender
```


### Install Dependencies
   
This project uses the python-dotenv library to manage environment variables. Install it with pip:



``
pip install python-dotenv
``



### Edit your credentials 
```
sender_email = "your_email@example.com"
password = "your_secure_app_password"
```


### Edit the Email Template
   
You can customize the email content by editing the HTML template in the script. Open the gMAIL.py file and adjust the email body according to your needs.

The {name} placeholder will be replaced by each recipient's name when the program runs.



### Add Recipients
   
You can add a list of recipients (name and email) in the script like this:

```
recipients = [
    {"email": "example1@example.com", "name": "Brooke"},
    {"email": "example2@example.com", "name": "Alice"},
    {"email": "example3@example.com", "name": "Sophia"}
]
```
Each email will be personalized with the name of the recipient.



### Run the Script

Now that everything is set up, you can run the script to send emails. Ensure you're in the project directory, then run:

``
python gMAIL.py
``


If everything is configured correctly, the script will start sending emails to your recipients.
