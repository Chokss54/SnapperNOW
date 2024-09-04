import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, html_content):
  message = MIMEMultipart("alternative")
  message["From"] = sender_email
  message["To"] = ', '.join(receiver_email)
  message["Subject"] = "Snapper Season Alert!"
  message.attach(MIMEText(html_content, "html"))

  try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
  except smtplib.SMTPAuthenticationError:
    print("Authentication error. Check your email and password.")
  except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
  finally:
    server.quit()
