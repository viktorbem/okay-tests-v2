import __main__
import os
import smtplib
import time
import sys

from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image
from selenium import webdriver
from slack_sdk.webhook import WebhookClient


MAILFROM = ""
MAILTO = ""
PASSWORD = ""
SLACK_URL = ""


class Maintest:
    def __init__(self, name=None, is_mobile=False, is_headless=False, is_email=False, is_slack=False, delay=10, **kwargs):
        self.testname = name
        if not self.testname:
            self.testname = os.path.basename(sys.argv[0][:-3])
        self.step = "Initialize maintest"
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.rootpath = os.path.abspath(os.path.dirname(__name__))
        self.logpath = os.path.join(self.rootpath, "logs", self.date, self.testname)
        if not os.path.exists(self.logpath):
            os.makedirs(self.logpath)
        
        self.is_mobile = is_mobile
        self.is_headless = is_headless
        self.is_email = is_email
        self.is_slack = is_slack
        self.default_delay = delay

        if os.name == "nt":
            self.driver = self.setup_chrome(os.path.join(self.rootpath, "chromedriver.exe"))
        else:
            self.driver = self.setup_chrome("/usr/bin/chromedriver")
    
    def setup_chrome(self, driver):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--lang=en")
        if self.is_mobile:
            width = 360
            height = width * 3
            mobile = {"deviceName": "iPhone X"}
            self.options.add_experimental_option("mobileEmulation", mobile)
        else:
            width = 1920
            height = width * 2
        if self.is_headless:
            self.options.add_argument("--headless")
        new_driver = webdriver.Chrome(driver, chrome_options=self.options)
        new_driver.set_window_size(width=width, height=height)
        return new_driver
    
    def sleep(self, custom_delay=None):
        """self.sleep(delay=Int)"""
        if custom_delay:
            time.sleep(custom_delay)
        else:
            time.sleep(self.default_delay)

    def click(self, element):
        """self.click(element=WebdriverObject)"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def send_keys_slowly(self, element, text):
        """self.send_keys_slowly(element=WebdriverObject, text=Str)"""
        for char in text:
            element.send_keys(char)
            self.sleep(1)

    def abort(self):
        """Close the browser window and exit the test."""
        self.driver.close()

    def log(self, step):
        """self.log(message=Str)"""
        self.step = f"Func: {sys._getframe(1).f_code.co_name} >> {step}"
    
    def take_screenshot(self, timestamp="", type="src"):
        """self.take_screenshot(timestamp=DatetimeObject, type=Str)"""
        if timestamp == '':
            timestamp = datetime.now().strftime("%H%M%S")
        filename = f"{timestamp}_{type}"
        png_img = os.path.join(self.logpath, f"{filename}.png")
        self.driver.save_screenshot(png_img)
        with Image.open(png_img) as rgba_img:
            jpg_img = os.path.join(self.logpath, f"{filename}.jpg")
            rgb_img = rgba_img.convert("RGB")
            rgb_img.save(jpg_img, optimize=True, quality=30)
        os.remove(png_img)
    
    def log_error(self, message, during="Unidentified error"):
        """self.log_error(message=Str, during=Str)"""
        msg = f"{during}\n\n{message}"
        print(msg)
        timestamp = datetime.now().strftime("%H%M%S")
        self.take_screenshot(timestamp, "err")
        with open(os.path.join(self.logpath, f"{timestamp}_err.txt"), "w") as logfile:
            logfile.write(msg)

        # Send email if test crashes
        if self.is_email:
            new_msg = MIMEMultipart()
            new_msg["From"] = MAILFROM
            new_msg["To"] = MAILTO
            new_msg["Subject"] = self.testname
            new_msg.attach(MIMEText(f"\n\n{message}", "plain"))

            filename = f"{timestamp}_err.jpg"
            path_to_img = os.path.join(self.logpath, filename)
            payload = MIMEBase("application", "octate-stream")
            with open(path_to_img, "rb") as file:
                payload.set_payload(file.read())
                encoders.encode_base64(payload)
                payload.add_header("Content-Disposition", "attachement", filename=filename)
                new_msg.attach(payload)
            text = new_msg.as_string()

            with smtplib.SMTP("smtp.gmail.com") as mailserver:
                mailserver.starttls()
                mailserver.login(user=MAILFROM, password=PASSWORD)
                mailserver.sendmail(
                    from_addr=MAILFROM,
                    to_addrs=MAILTO,
                    msg=text
                )

        # Send message to Slack if test crashes
        if self.is_slack:
            webhook = WebhookClient(SLACK_URL)    
            response = webhook.send(text=f"*{self.testname} >>* {msg}")
            print(response.status_code)
        

if __name__ == "__main__":
    pass