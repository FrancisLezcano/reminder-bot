# Receipt Reminder Bot

A Python tool that automatically sends email reminders for missing receipts.  
Designed to help small businesses track employee expenses and ensure all receipts are submitted.

## Features
- Reads expense data from a CSV file
- Sends customized reminder emails for missing receipts
- Updates CSV after reminders are sent to avoid duplicates

## How It Works
1. You maintain an expenses.csv with expense records.
2. The bot checks for entries marked as "No" under ReceiptReceived.
3. It sends an email to the associated address.
4. Updates the CSV to mark them as reminded.

## Skills Demonstrated
- Python scripting
- CSV file handling
- Email automation (SMTP)
- Data processing
- Basic automation for business workflow

## How to Run
bash
pip install -r requirements.txt
python reminder_bot.py
## Setup
1. Create a `.env` file in the project root with:
SENDER_EMAIL=your_email@example.com
SENDER_PASSWORD=your_app_password
2. Make sure `.env` is listed in `.gitignore` so secrets are never uploaded to GitHub.
