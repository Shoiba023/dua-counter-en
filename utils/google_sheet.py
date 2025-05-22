import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

# .env فائل سے API کی معلومات حاصل کریں
load_dotenv()

SHEET_NAME = os.getenv("SHEET_NAME")
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_JSON")

# Google Sheet کنیکشن
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

def get_dua_counts():
    records = sheet.get_all_records()
    return records

def add_dua_entry(name, dua, count):
    sheet.append_row([name, dua, count])
