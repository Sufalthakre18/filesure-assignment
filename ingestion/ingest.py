import pandas as pd
import re
import os
from pymongo import MongoClient
from dateutil import parser
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["filesure"]
collection = db["companies"]

df = pd.read_csv("../data/company_records.csv")

def parse_date(date):
    try:
        return parser.parse(str(date)).isoformat()
    except:
        return None

def clean_status(status):
    if not status:
        return None
    s = str(status).lower()

    if "active" in s:
        return "Active"
    if "strike" in s:
        return "Strike Off"
    if "liquid" in s:
        return "Under Liquidation"
    if "dormant" in s:
        return "Dormant"
    return "Unknown"

def clean_capital(value):
    if pd.isna(value):
        return None
    value = re.sub(r"[^\d]", "", str(value))
    return int(value) if value else None

def validate_email(email):
    if pd.isna(email):
        return None, False

    email = str(email).strip()
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return email, bool(re.match(pattern, email))

records = []

for _, row in df.iterrows():
    email, is_valid = validate_email(row.get("email"))

    record = {
        "cin": row.get("cin") if pd.notna(row.get("cin")) else None,
        "company_name": row.get("company_name"),
        "status": clean_status(row.get("status")),
        "incorporation_date": parse_date(row.get("incorporation_date")),
        "state": row.get("state"),
        "directors": [
            row.get("director_1"),
            row.get("director_2")
        ],
        "paid_up_capital": clean_capital(row.get("paid_up_capital")),
        "last_filing_date": parse_date(row.get("last_filing_date")),
        "email": email,
        "is_email_valid": is_valid
    }

    records.append(record)

collection.delete_many({})
collection.insert_many(records)

collection.create_index([("status", 1), ("state", 1)])

print("✅ Data inserted into MongoDB Atlas")