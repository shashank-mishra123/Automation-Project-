from pathlib import Path

DATA_DIR = Path("data")
LOGS_DIR = Path("logs")
REPORTS_DIR = Path("reports")

CONTACTS_FILE = DATA_DIR / "contacts.csv"
SENT_REPORT_FILE = REPORTS_DIR / "sent.csv"
FAILED_REPORT_FILE = REPORTS_DIR / "failed.csv"

WHATSAPP_WEB_URL = "https://web.whatsapp.com"
DEFAULT_MESSAGE = "Hello {{name}}, welcome to our service."
DELAY_MIN = 10
DELAY_MAX = 20

LOG_FILE = LOGS_DIR / "app.log"
