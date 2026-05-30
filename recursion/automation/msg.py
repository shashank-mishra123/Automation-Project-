import argparse
import os
import re
import time
from typing import List, Optional

import pandas as pd
import pywhatkit as kit

CSV_FILE = "number.csv"
MAX_MESSAGES = 1
MESSAGE = """Congratulations! Your Selection is Confirmed*

Congratulations. Your selection is confirmed for the training at Lunetron web services.

This is the LAST SUMMER TRAINING BATCH of 2026.

We have a short induction session today at 07:00 PM
Maybe you are in the gym, college, market, or office — no problem. Just join the session (approx. 30 minutes). It’s important and will help you understand everything about the training.

Training Details:
• Duration: UP TO 01 MONTHS
• Mode: Online

Join WhatsApp group:
https://chat.whatsapp.com/KaTX3Yg5NCG2LcBQ9doSo4

Please try to join on time. This will help you move to the next step.



Anup Mishra
Lunetron web services"""

WAIT_TIME = 30
TAB_CLOSE = True
CLOSE_TIME = 10


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send WhatsApp messages to all valid phone numbers from number.csv"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--test",
        action="store_true",
        help="Send one test message to the first valid phone number",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Send messages to all valid phone numbers",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove invalid phone numbers from the CSV before sending",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show target phone numbers and actions without actually sending messages",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=1,
        help="Maximum number of messages to send in test mode",
    )

    args = parser.parse_args()
    if not args.test and not args.all:
        args.all = True
    return args


def save_cleaned_numbers(phone_numbers: List[str], csv_path: str) -> None:
    df = pd.DataFrame({"phone": phone_numbers})
    df.to_csv(csv_path, index=False)
    print(f"Cleaned CSV saved with {len(phone_numbers)} valid numbers: {csv_path}")


def normalize_phone(raw_phone: str) -> Optional[str]:
    phone = str(raw_phone).strip()
    if not phone or phone.lower() == "nan":
        return None

    if phone.endswith(".0") and phone.replace(".", "").isdigit():
        phone = phone[:-2]

    phone = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    if phone.startswith("+"):
        digits = re.sub(r"[^0-9]", "", phone[1:])
        if len(digits) < 10:
            return None
        return "+" + digits

    digits = re.sub(r"[^0-9]", "", phone)
    if not digits:
        return None

    if digits.startswith("0"):
        digits = digits.lstrip("0")

    if len(digits) == 10:
        return "+91" + digits
    if len(digits) == 12 and digits.startswith("91"):
        return "+" + digits

    return None


def get_csv_path() -> str:
    return os.path.join(os.path.dirname(__file__), CSV_FILE)


def extract_phone_candidates(raw_phone: str) -> List[str]:
    if raw_phone is None:
        return []

    raw_text = str(raw_phone).strip()
    if not raw_text:
        return []

    candidates = re.split(r"[\n,;]+", raw_text)
    return [candidate.strip() for candidate in candidates if candidate.strip()]


def get_valid_phone_numbers(data) -> List[str]:
    phone_numbers: List[str] = []
    seen: set[str] = set()

    for raw_phone in data["phone"]:
        for candidate in extract_phone_candidates(raw_phone):
            normalized = normalize_phone(candidate)
            if normalized and normalized not in seen:
                seen.add(normalized)
                phone_numbers.append(normalized)
            elif not normalized:
                print(f"Skipping invalid phone value: {candidate}")

    return phone_numbers


def send_messages(phone_numbers: List[str], dry_run: bool) -> None:
    print("Ready to send messages to:")
    for phone in phone_numbers:
        print(f" - {phone}")

    print("\nMake sure WhatsApp Web is open in your browser and you are logged in.")
    time.sleep(3)

    for phone in phone_numbers:
        if dry_run:
            print(f"Dry run: would send message to {phone}")
            continue

        try:
            print(f"Sending message to {phone}...")
            kit.sendwhatmsg_instantly(
                phone_no=phone,
                message=MESSAGE,
                wait_time=WAIT_TIME,
                tab_close=TAB_CLOSE,
                close_time=CLOSE_TIME,
            )
            print(f"Message sent to {phone}")
            time.sleep(15)
        except Exception as e:
            print(f"Failed for {phone}: {e}")
            time.sleep(5)

    print("All messages processed.")


def main() -> None:
    args = parse_arguments()

    csv_path = get_csv_path()
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    data = pd.read_csv(csv_path, dtype=str, keep_default_na=False)

    if "phone" not in data.columns:
        raise ValueError("CSV file must have a 'phone' column")

    phone_numbers = get_valid_phone_numbers(data)
    if not phone_numbers:
        print("No valid phone numbers found in CSV.")
        return

    if args.clean:
        save_cleaned_numbers(phone_numbers, csv_path)
        if not args.all and not args.test:
            return

    if not phone_numbers:
        print("No valid phone numbers found in CSV.")
        return

    send_messages(phone_numbers, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
