import smtplib
from email.message import EmailMessage

# Define the function to read the email content
def message():
    # Specify 'utf-8' encoding to avoid UnicodeDecodeError
    with open(r'D:\Works\Alnafi\DCCS\7.  Python\Python Automation\Email\message.txt', encoding='utf-8') as content:
        data = content.read()
        return data

# Set up email details
my_mail = "abdullahabrar4843@gmail.com"
password = "rkmugbrwwaknyvgm"  # Consider storing this securely, not hardcoding

# Create an EmailMessage object
msg = EmailMessage()
msg['Subject'] = "System Setup Startup Notification"
msg['From'] = my_mail
msg['To'] = my_mail
msg['Cc'] = 'abdullah524278@gmail.com'

# Set the content of the email
msg.set_content(message())

# Set up SMTP connection using SSL for security
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=my_mail, password=password)
        connection.send_message(msg)
except Exception as e:
    print(f"Error occurred: {e}")
