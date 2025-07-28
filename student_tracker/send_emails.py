#!/usr/bin/python3

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========================
# CONFIGURATION
# ========================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "mordecaijeremy@gmail.com"
EMAIL_PASSWORD = os.getenv("pass")
EXCEL_PATH = "recipients.xlsx"
EMAIL_COLUMN = "Email"  # Column containing email addresses
SUBJECT = "Personalized Info Update"

# ========================
# EMAIL FUNCTION
# ========================
def send_bulk_emails():
    try:
        df = pd.read_excel(EXCEL_PATH)

        if EMAIL_COLUMN not in df.columns:
            print(f"ERROR: Column '{EMAIL_COLUMN}' not found in Excel.")
            return

        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        for _, row in df.iterrows():
            recipient = row[EMAIL_COLUMN]
            if pd.isna(recipient):
                continue

            # Create dynamic body from the rest of the columns
            body_lines = []
            for col in df.columns:
                if col != EMAIL_COLUMN:
                    body_lines.append(f"{col}: {row[col]}")
            message_body = "\n".join(body_lines)

            # Compose email
            msg = MIMEMultipart()
            msg['From'] = EMAIL_SENDER
            msg['To'] = recipient
            msg['Subject'] = SUBJECT
            msg.attach(MIMEText(message_body, 'plain'))

            # Send email
            server.sendmail(EMAIL_SENDER, recipient, msg.as_string())
            print(f"Email sent to {recipient}")

        server.quit()
        print("✅ All emails sent successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")

# ========================
# MAIN
# ========================
if __name__ == "__main__":
    send_bulk_emails()

