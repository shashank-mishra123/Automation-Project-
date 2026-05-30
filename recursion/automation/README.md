# WhatsApp Automation

This folder contains a small WhatsApp messaging automation tool.

## Files

- `msg.py` — main script for reading phone numbers and sending messages
- `number.csv` — phone number list with a `phone` header
- `send_all_messages.bat` — run the script in full send mode
- `test_send_message.bat` — run the script in test mode

## Requirements

- Python 3.8 or higher
- `pandas`
- `pywhatkit`

Install dependencies with:

```bash
pip install pandas pywhatkit
```

## Usage

From this directory:

```bash
python msg.py --dry-run --all
```

Options:

- `--all`: send messages to all valid phone numbers
- `--test`: send a message to the first valid number
- `--clean`: clean invalid phone numbers from `number.csv`
- `--dry-run`: show targets without sending messages

## Notes

- Open WhatsApp Web and log in before running the script
- Use `--dry-run` first to verify the numbers
