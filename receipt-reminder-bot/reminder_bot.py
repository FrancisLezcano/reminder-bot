import csv
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

# Load variables from .env
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
CSV_FILE = os.getenv("CSV_FILE")

def send_email(to_address, cardholder, amount, vendor, date):
    subject = "Missing Receipt Reminder"
    body = f"""Hi {cardholder},

We noticed a charge of ${amount} at {vendor} on {date} that does not have a receipt on file.

Please upload or forward your receipt at your earliest convenience.

Thanks,
Danny & Ron's Rescue Team
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_address

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_address, msg.as_string())
        server.quit()
        print(f"✅ Reminder sent to {cardholder} ({to_address})")
        return True
    except Exception as e:
        print(f"❌ Failed to send email to {cardholder}: {e}")
        return False

def process_csv(filename):
    rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["ReceiptReceived"].strip().lower() == "no":
                success = send_email(
                    to_address=row["Email"],
                    cardholder=row["Cardholder"],
                    amount=row["Amount"],
                    vendor=row["Vendor"],
                    date=row["Date"]
                )
                if success:
                    row["ReceiptReceived"] = "yes"
            rows.append(row)

    # Write updated rows back to CSV
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    process_csv(CSV_FILE)
