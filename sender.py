import logging
import os
import random
import time
import urllib.parse
from pathlib import Path

import pyautogui
import pywhatkit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from config import DELAY_MAX, DELAY_MIN, WHATSAPP_WEB_URL
from utils import build_message, validate_phone_number


class WhatsAppSender:
    def __init__(self, logger: logging.Logger, headless: bool = False, profile_dir: str = "whatsapp_profile"):
        self.logger = logger
        self.headless = headless
        self.profile_dir = profile_dir
        self.driver = None
        try:
            self.driver = self._init_driver()
        except Exception as exc:
            self.logger.warning("Unable to start Selenium Chrome driver: %s", exc)
            self.logger.warning("Falling back to pywhatkit-based message delivery.")

    def _init_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-allow-origins=*")
        options.add_argument("--disable-features=RendererCodeIntegrity")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")

        profile_path = Path(self.profile_dir).resolve()
        profile_path.mkdir(parents=True, exist_ok=True)
        options.add_argument(f"--user-data-dir={profile_path}")

        chrome_path = os.environ.get(
            "CHROME_PATH",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        )
        if Path(chrome_path).exists():
            options.binary_location = chrome_path

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        return driver

    def open_whatsapp_web(self):
        if not self.driver:
            self.logger.info("Selenium driver unavailable. Skipping WhatsApp Web initialization.")
            return
        self.driver.get(WHATSAPP_WEB_URL)
        self.logger.info("Opening WhatsApp Web and waiting for session login.")
        self._wait_for_login()
# login 
    def _wait_for_login(self):
        self.logger.info("Waiting for WhatsApp Web login state.")
        end_time = time.time() + 60
        while time.time() < end_time:
            if self.driver.find_elements(By.XPATH, "//div[@id='pane-side']"):
                self.logger.info("WhatsApp Web session is already logged in.")
                return
            if self.driver.find_elements(By.XPATH, "//canvas[@aria-label='Scan me!']"):
                self.logger.info("Waiting for QR code scan and login.")
            time.sleep(2)

        end_time = time.time() + 180
        while time.time() < end_time:
            if self.driver.find_elements(By.XPATH, "//div[@id='pane-side']"):
                self.logger.info("WhatsApp Web login completed.")
                return
            time.sleep(2)

        self.logger.error("Unable to detect WhatsApp Web login within the expected time.")
        raise RuntimeError("WhatsApp Web login required.")

    def _click_send(self):
        candidate_selectors = [
            "//button[@data-testid='compose-btn-send']",
            "//button[contains(@class, 'compose-btn-send')]",
            "//span[@data-icon='send']",
            "//button[@title='Send']",
        ]
        for selector in candidate_selectors:
            try:
                button = self.driver.find_element(By.XPATH, selector)
                button.click()
                return True
            except NoSuchElementException:
                continue
        return False

    def _send_via_whatsapp_url(self, phone_number: str, message: str) -> None:
        encoded_message = urllib.parse.quote(message)
        send_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
        self.driver.get(send_url)
        self.logger.debug("Navigated to send URL for %s", phone_number)

        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
            )
            time.sleep(2)
            if not self._click_send():
                pyautogui.press("enter")
                self.logger.debug("Clicked send via keyboard for %s", phone_number)
        except TimeoutException:
            self.logger.warning("Send page did not load fast enough for %s. Using fallback method.", phone_number)
            raise

    def _send_via_pywhatkit(self, phone_number: str, message: str) -> None:
        self.logger.debug("Sending message with pywhatkit fallback for %s", phone_number)
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True, close_time=3)

    def send_contact_message(self, contact: dict, template: str) -> dict:
        phone_number = contact.get("phone", "")
        if not validate_phone_number(phone_number):
            self.logger.warning("Invalid phone number skipped: %s", phone_number)
            return {"status": "failed", "reason": "invalid_phone", **contact}

        message = build_message(template, contact)
        if not self.driver:
            self.logger.info("Sending via pywhatkit directly because Selenium is unavailable.")
            try:
                self._send_via_pywhatkit(phone_number, message)
                self.logger.info("Message sent using fallback pywhatkit for %s", phone_number)
                return {"status": "sent", "message": message, **contact}
            except Exception as fallback_error:
                self.logger.error("Failed to send message to %s with pywhatkit: %s", phone_number, fallback_error)
                return {
                    "status": "failed",
                    "reason": str(fallback_error),
                    "message": message,
                    **contact,
                }

        try:
            self._send_via_whatsapp_url(phone_number, message)
            time.sleep(random.uniform(2, 4))
            self.logger.info("Message sent to %s", phone_number)
            return {"status": "sent", "message": message, **contact}
        except Exception as first_error:
            self.logger.warning("Primary send failed for %s: %s", phone_number, first_error)
            try:
                self._send_via_pywhatkit(phone_number, message)
                self.logger.info("Message sent using fallback pywhatkit for %s", phone_number)
                return {"status": "sent", "message": message, **contact}
            except Exception as fallback_error:
                self.logger.error("Failed to send message to %s: %s", phone_number, fallback_error)
                return {
                    "status": "failed",
                    "reason": str(fallback_error),
                    "message": message,
                    **contact,
                }

    def send_bulk_messages(self, contacts: list[dict], template: str, delay_min: int = DELAY_MIN, delay_max: int = DELAY_MAX) -> tuple[list[dict], list[dict]]:
        sent_records = []
        failed_records = []
        for idx, contact in enumerate(contacts, start=1):
            self.logger.info("Processing contact %d/%d: %s", idx, len(contacts), contact.get("phone"))
            result = self.send_contact_message(contact, template)
            if result.get("status") == "sent":
                sent_records.append(result)
            else:
                failed_records.append(result)

            delay = random.randint(delay_min, delay_max)
            self.logger.info("Waiting %s seconds before the next message.", delay)
            time.sleep(delay)

        return sent_records, failed_records

    def close(self):
        if self.driver:
            self.driver.quit()
            self.logger.info("WhatsApp browser session closed.")
