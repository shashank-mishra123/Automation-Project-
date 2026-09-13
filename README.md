# WhatsApp Bulk Messaging Automation Agent

A backend-only Python automation project to send WhatsApp messages to a list of contacts loaded from CSV or Excel files.

## Features

- Read contacts from `CSV` or `Excel` files
- Normalize and validate phone numbers 
- Send the same message to all contacts 
- Send personalized messages using `{{name}}` and other placeholders
- Generate logs and reports for sent and failed messages 
- Add random delay between messages to reduce spam detection risk
- One-command execution via `python main.py`

## Requirements

- Python 3.11+
- Chrome browser installed

### Python dependencies

Install required libraries:

```bash
pip install -r requirements.txt
```

## Project Structure

```
whatsapp_agent/
│
├── main.py
├── sender.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   └── contacts.csv
│
├── logs/
│   └── app.log
│
└── reports/
    ├── sent.csv
    └── failed.csv
```

## CSV / Excel Format

The input file must include at least a `phone` column. A `name` column is recommended for personalization.

Example `contacts.csv`:

```csv
name,phone
Shashank,+919876543210
Rahul,+919812345678
```

## Usage

Run the automation:

```bash
python main.py
```

Optional arguments:

```bash
python main.py --file data/contacts.csv --message "Hello {{name}}, welcome to our service." --delay-min 10 --delay-max 20
```

### Arguments

- `--file`, `-f`: Path to a CSV or Excel file containing contacts
- `--message`, `-m`: Message template with placeholders like `{{name}}`
- `--delay-min`: Minimum delay between messages in seconds
- `--delay-max`: Maximum delay between messages in seconds
- `--headless`: Use headless browser mode (not recommended for QR login)

## Output

- `logs/app.log` — detailed application logs
- `reports/sent.csv` — records of successfully sent messages
- `reports/failed.csv` — records of messages that failed to send

## Notes

- WhatsApp Web login is required on first run
- The browser profile is stored in `./whatsapp_profile`
- Headless mode may not work reliably for WhatsApp Web login

## Troubleshooting

- Ensure Chrome is installed and accessible
- If `contacts.csv` is missing or invalid, the script will report an error
- For best results, keep delays between messages to avoid rate limiting
