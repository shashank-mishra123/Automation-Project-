import csv
import logging
import re
from pathlib import Path

import pandas as pd

from config import CONTACTS_FILE, DATA_DIR, LOGS_DIR, REPORTS_DIR, SENT_REPORT_FILE, FAILED_REPORT_FILE


def ensure_directories() -> None:
    for path in (DATA_DIR, LOGS_DIR, REPORTS_DIR):
        path.mkdir(parents=True, exist_ok=True)


def init_logger(log_file: Path) -> logging.Logger:
    logger = logging.getLogger("whatsapp_agent")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def normalize_phone_number(raw_phone: str) -> str:
    if raw_phone is None:
        return ""
    phone = str(raw_phone).strip()
    phone = re.sub(r"[()\s-]+", "", phone)
    phone = re.sub(r"^00", "+", phone)
    if phone and not phone.startswith("+"):
        phone = "+" + phone
    return phone


def validate_phone_number(phone: str) -> bool:
    if not phone:
        return False
    if not re.fullmatch(r"\+[0-9]{8,15}", phone):
        return False
    return True


def load_contacts(file_path: Path) -> list[dict]:
    if not file_path.exists():
        raise FileNotFoundError(f"Contact file not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(file_path, dtype=str)
    elif suffix in (".xls", ".xlsx"):
        df = pd.read_excel(file_path, dtype=str)
    else:
        raise ValueError("Unsupported contact file type. Use CSV or Excel.")

    expected_columns = {"phone", "name"}
    available_columns = {col.strip().lower() for col in df.columns}
    if "phone" not in available_columns:
        raise ValueError("Input data must contain a 'phone' column.")

    df = df.rename(columns={col: col.strip().lower() for col in df.columns})
    df = df.fillna("")
    contacts = []
    for _, row in df.iterrows():
        raw_phone = row.get("phone", "")
        phone = normalize_phone_number(raw_phone)
        name = str(row.get("name", "")).strip()
        if not raw_phone or not phone:
            continue
        contact = {"phone": phone, "name": name}
        contact.update({k: str(v).strip() for k, v in row.items() if k not in ("phone", "name")})
        contacts.append(contact)

    return [c for c in contacts if c["phone"]]


def build_message(template: str, contact: dict) -> str:
    message = str(template)
    for key, value in contact.items():
        placeholder = f"{{{{{key}}}}}"
        message = message.replace(placeholder, str(value))
    return message


def save_report(report_path: Path, records: list[dict], fieldnames: list[str]) -> None:
    if not records:
        with report_path.open("w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        return

    with report_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
