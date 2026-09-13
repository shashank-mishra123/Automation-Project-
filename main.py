import argparse
import sys
from pathlib import Path

from config import CONTACTS_FILE, DEFAULT_MESSAGE, FAILED_REPORT_FILE, LOG_FILE, SENT_REPORT_FILE
from sender import WhatsAppSender
from utils import ensure_directories, init_logger, load_contacts, save_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("WhatsApp Bulk Messaging Automation Agent")
    parser.add_argument("--file", "-f", default=str(CONTACTS_FILE), help="Path to contacts CSV or Excel file.")
    parser.add_argument("--message", "-m", default=DEFAULT_MESSAGE, help="Message template to send. Use {{name}} placeholders.")
    parser.add_argument("--delay-min", type=int, default=10, help="Minimum delay between messages in seconds.")
    parser.add_argument("--delay-max", type=int, default=20, help="Maximum delay between messages in seconds.")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode. WhatsApp Web may require a visible browser for login.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_directories()
    logger = init_logger(Path(LOG_FILE))

    try:
        contact_path = Path(args.file)
        contacts = load_contacts(contact_path)
        if not contacts:
            logger.error("No valid contacts found in %s", contact_path)
            print("No valid contacts found. Check the input file and contacts format.")
            return 1

        sender = WhatsAppSender(logger=logger, headless=args.headless)
        try:
            sender.open_whatsapp_web()
            sent_records, failed_records = sender.send_bulk_messages(
                contacts=contacts,
                template=args.message,
                delay_min=args.delay_min,
                delay_max=args.delay_max,
            )
        finally:
            # close 
            sender.close()

        save_report(Path(SENT_REPORT_FILE), sent_records, ["name", "phone", "message", "status"])
        save_report(Path(FAILED_REPORT_FILE), failed_records, ["name", "phone", "message", "status", "reason"])

        print(f"Summary: {len(sent_records)} sent, {len(failed_records)} failed.")
        logger.info("Bulk send completed. Sent=%d Failed=%d", len(sent_records), len(failed_records))
        if failed_records:
            print(f"See {FAILED_REPORT_FILE} for failed records.")
        return 0
    except Exception as exc:
        logger.exception("An error occurred while running the bulk sender.")
        print(f"Error: {exc}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
