import smtplib
from email.mime.text import MIMEText

# Generate a TOTP
otp = generate_otp(secret)

# Send the email
sender = "noreply@example.com"
receiver = "user@example.com"
subject = "One-Time Password"
body = f"Your OTP is: {otp}"
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP("smtp.example.com")
server.sendmail(sender, [receiver], msg.as_string())
server.quit()
