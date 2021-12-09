import __main__
import json
import os
import requests
import smtplib
import sys
import time

from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image
from selenium import webdriver
from slack_sdk import WebClient
from types import SimpleNamespace


with open(os.path.join(os.path.abspath(os.path.dirname(__name__)), "config.json")) as json_file:
    data = json.loads(json_file.read(), object_hook=lambda kwargs: SimpleNamespace(**kwargs))
    DEFAULT, SECRET = data.defaults, data.secrets


class MainTest:
    def __init__(
        self, name=None, theme="", is_mobile=0, delay=int(DEFAULT.delay), is_headless=bool(DEFAULT.is_headless),
        is_email=bool(DEFAULT.is_email), is_slack=bool(DEFAULT.is_slack), **kwargs
    ):
        self.testname = name
        if not self.testname:
            self.testname = os.path.basename(sys.argv[0][:-3])
        self.step = "Initialize maintest"
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.now().strftime("%H%M%S")
        self.rootpath = os.path.abspath(os.path.dirname(__name__))
        self.logpath = os.path.join(self.rootpath, "logs", self.date, self.testname)
        
        self.home_url = ""
        self.product_name = ""
        self.theme = theme
        self.errors = True
        self.screenshots = True

        if not os.path.exists(self.logpath):
            os.makedirs(self.logpath)
        
        self.is_mobile = is_mobile
        self.is_headless = is_headless
        self.is_email = is_email
        self.is_slack = is_slack
        self.default_delay = delay

        self.driver = self.setup_chrome()
    
    def setup_chrome(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--lang=en")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
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

        if os.name == "nt":
            driver = os.path.join(self.rootpath, "chromedriver.exe")
        else:
            driver = "/usr/bin/chromedriver"
        new_driver = webdriver.Chrome(driver, chrome_options=self.options)
        new_driver.set_window_size(width=width, height=height)
        return new_driver

    def set_dev_theme(self, theme):
        dev_url = f"{self.home_url}/?preview_theme_id={theme}"
        response = requests.get(dev_url)
        if response.status_code == 200:
            print("DEV ENVIRONMENT ----------")
            self.driver.get(dev_url)
        self.sleep(5)

    def sleep(self, custom_delay=None):
        """self.sleep(delay=Int)"""
        if custom_delay:
            time.sleep(custom_delay)
        else:
            time.sleep(self.default_delay)

    def click(self, element):
        """self.click(element=WebdriverObject)"""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def send_keys_slowly(self, element, text):
        """self.send_keys_slowly(element=WebdriverObject, text=Str)"""
        for char in text:
            element.send_keys(char)
            self.sleep(1)

    def abort(self):
        """
        Close the browser window and exit the test.
        
        Example:
        - test.abort()
        """
        self.driver.close()

    def log(self, step):
        """self.log(message=Str)"""
        self.step = f"Func: {sys._getframe(1).f_code.co_name} >> {step}"

    def new_test(self):
        """
        Set default values for test during each iteration, clear cache and cookies.
        It is meant to be run in 'for' loops at the beginning of each test.

        Example:
        - test.new_test()
        """
        self.errors = True
        self.driver.delete_all_cookies()
    
    def take_screenshot(self, timestamp="", type="src"):
        """self.take_screenshot(timestamp=DatetimeObject, type=Str)"""
        if not self.screenshots:
            return
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
    
    def log_results(self, name, url, logs, screenshots=True):
        """
        Logs any number of dictionaries with key: value pairs into a log file.

        Example:
        - test.log_results(
            name='(2) Do 50 kg', 
            url='https://www.okay.sk/collections/mikrovlnne-rury-a-mini-rury',
            logs=[
                {'Zásielkovňa': '1,00 €', 'Doručiť na moju adresu': '2,00& €'},
                {'Bankový prevod': '-', 'Dobierka': '0 €', 'Platba na výdajni': '-'}
            ]
        )

        All arguments are mandatory.
        """
        self.screenshots = screenshots
        result = f"|{'=' * 90}\n| {name}\n| {url}\n"
        for log in logs:
            if not log:
                continue
            result += f"|{'-' * 90}\n"
            for key, value in log.items():
                if len(key) > 45:
                    row_name = f"{key[:40]}..."
                else:
                    row_name = key
                spacing = " " * (50 - len(row_name))
                result += f"| {row_name}{spacing}{value}\n"
        result += f"|{'=' * 90}\n"
        print(result)
        filename = f"{self.time}_log.txt"
        with open(os.path.join(self.logpath, filename), "a", encoding="utf-8") as logfile:
            logfile.write(result)

    def log_error(self, message, during="Unidentified error"):
        """self.log_error(message=Str, during=Str)"""
        self.errors = False
        message = str(message).split("Stacktrace:")[0]
        msg = f"ERR during >> {during}\n\n{message}"
        print(msg)
        timestamp = datetime.now().strftime("%H%M%S")
        self.take_screenshot(timestamp, "err")
        with open(os.path.join(self.logpath, f"{timestamp}_err.txt"), "w", encoding="utf-8") as logfile:
            logfile.write(msg)

        filename = f"{timestamp}_err.jpg"
        path_to_img = os.path.join(self.logpath, filename)

        # Send email if test crashes
        if self.is_email:
            new_msg = MIMEMultipart()
            new_msg["From"] = SECRET.mail_from
            new_msg["To"] = SECRET.mail_to
            new_msg["Subject"] = self.testname
            new_msg.attach(MIMEText(f"\n\n{message}", "plain"))

            payload = MIMEBase("application", "octate-stream")
            with open(path_to_img, "rb") as file:
                payload.set_payload(file.read())
                encoders.encode_base64(payload)
                payload.add_header("Content-Disposition", "attachement", filename=filename)
                new_msg.attach(payload)
            text = new_msg.as_string()

            with smtplib.SMTP("smtp.gmail.com") as mailserver:
                mailserver.starttls()
                mailserver.login(user=SECRET.mail_from, password=SECRET.mail_password)
                mailserver.sendmail(
                    from_addr=SECRET.mail_from,
                    to_addrs=SECRET.mail_to,
                    msg=text
                )

        # Send message to Slack if test crashes
        if self.is_slack:
            client = WebClient(SECRET.slack_token)
            response = client.files_upload(
                channels=SECRET.slack_channel,
                initial_comment=f"*{self.testname} >>* {msg}",
                file=path_to_img
            )
            print(response.status_code)
        

if __name__ == "__main__":
    pass