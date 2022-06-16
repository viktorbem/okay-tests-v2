import __main__
import functools
import json
import os
import pprint
import random
import re
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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from slack_sdk import WebClient
from types import SimpleNamespace


with open(os.path.join(os.path.abspath(os.path.dirname(__main__.__file__)), 'config.json')) as json_file:
    data = json.loads(json_file.read(), object_hook=lambda kwargs: SimpleNamespace(**kwargs))
    DEFAULT, SECRET = data.defaults, data.secrets


class MainTest:
    def __init__(
        self, name=None, theme='', is_mobile=0, delay=int(DEFAULT.delay), is_headless=bool(DEFAULT.is_headless),
        is_email=bool(DEFAULT.is_email), is_slack=bool(DEFAULT.is_slack), password='', **kwargs
    ):
        self.testname = name
        print(self.testname)
        self.shop_password = password
        if not self.testname:
            self.testname = os.path.basename(sys.argv[0][:-3])
        self.step = 'Initialize maintest'
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.time = datetime.now().strftime('%H%M%S')
        self.rootpath = os.path.abspath(os.path.dirname(__main__.__file__))
        self.logpath = os.path.join(self.rootpath, 'logs', self.date, self.testname)
        
        self.last_url = ''
        self.home_url = ''
        self.product_name = ''
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

        self.driver = None
        self.driver = self._setup_chrome()
    
    @staticmethod
    def catch_error(f):
        @functools.wraps(f)
        def inner(self, screenshots=True, *args, **kwargs):
            self.screenshots = screenshots
            if self.errors:
                try:
                    return f(self, *args, **kwargs)
                except Exception as err:
                    self.log_error(message=err, during=self.step)
        return inner

    def _setup_chrome(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--lang=en')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if self.is_mobile:
            width = 360
            height = width * 3
            mobile = {'deviceName': 'iPhone X'}
            self.options.add_experimental_option('mobileEmulation', mobile)
        else:
            width = 1920
            height = width * 2
        if self.is_headless:
            self.options.add_argument('--headless')

        if os.name == 'nt':
            driver = os.path.join(self.rootpath, 'chromedriver.exe')
        else:
            driver = '/usr/bin/chromedriver'
        logfile = os.path.join(self.logpath, f'{self.time}_log.txt')
        self.dc = DesiredCapabilities.CHROME
        self.dc['goog:loggingPrefs'] = {'browser': 'ALL'}
        try:
            new_driver = webdriver.Chrome(
                driver,
                chrome_options=self.options,
                desired_capabilities=self.dc,
                service_args=[f'--log-path={logfile}']
            )
        except Exception as err:
            self.log_error(err, during='Chromedriver init')
            sys.exit()
        new_driver.set_window_size(width=width, height=height)
        return new_driver

    def abort(self, screenshots=True):
        '''
        Close the browser window and exit the test.
        
        Example:
        - test.abort()
        '''
        with open(os.path.join(self.logpath, f'{self.time}_js.txt'), 'w', encoding='utf-8') as logfile:
            console_log = self.output_js_console()
            logfile.write(console_log)
        self.driver.close()

    def bypass_password(self, url):
        '''self.bypass_password(url=Str)'''
        self.driver.get(url)
        try:
            self.click(self.driver.find_element(By.CSS_SELECTOR, '#open-me a'))
        except Exception as err:
            print('No password needed ----------')
        else:
            self.driver.find_element(By.NAME, 'password').send_keys(self.shop_password)
            self.click(self.driver.find_element(By.NAME, 'commit'))
            self.sleep()

    def click(self, element, delay=False):
        '''self.click(element=WebdriverObject, delay=Bool)'''
        if delay:
            self.sleep()
        popups = self.driver.find_elements(By.CSS_SELECTOR, 'div[class*="box-promotion"]')
        for popup in popups:
            popup.find_element(By.CSS_SELECTOR, 'div button.close').click()
            self.sleep(5)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        element.click()

    def click_with_js(self, element, delay=False):
        '''self.click(element=WebdriverObject, delay=Bool)'''
        if delay:
            self.sleep()
        self.driver.execute_script('arguments[0].click();', element)

    def find_child_element(self, element, selector):
        '''
        Return the first child of the single element in argument that has the specified CSS selector.

        Example:
        - child = test.find_child_element(element=some_element, selector='.tag.on-order')

        Both arguments are mandatory.
        '''
        return element.find_element(By.CSS_SELECTOR, selector)

    def find_child_elements(self, element, selector):
        '''
        Return the list (array) of children of the single element in argument that satisfy the specified CSS selector.

        Example:
        - children = test.find_child_elements(element=some_element, selector='.tag.on-order')

        Both arguments are mandatory.
        '''
        return element.find_elements(By.CSS_SELECTOR, selector)

    def find_element(self, selector, screenshots=True):
        '''
        Return the first element on page with specified CSS selector as string.

        Example:
        - element = test.find_element(selector='.button--add-to-cart')

        The 'selector' argument is mandatory.
        '''
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def find_elements(self, selector, screenshots=True):
        '''
        Return the list (array) of elements on page that satisfy the CSS selector specified as string.

        Example:
        - elements = test.find_elements(selector='.button--add-to-cart')

        The 'selector' argument is mandatory.
        '''
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def get_random_words(self, items, screenshots=True):
        '''
        Return the list of randomly generated search words.
        Length of the list equals the number provided in 'items' argument.

        Example:
        - words = test.get_random_words(items=3)

        The 'items' argument is mandatory.
        '''
        web_key = 'okay'
        lang_key = 'cz'
        if 'jena' in self.home_url:
            web_key = 'jena'
        if 'sk' in self.home_url:
            lang_key = 'sk'
        
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'search.json')) as json_file:
                data = json.loads(json_file.read())
                search_words = data[web_key][lang_key]
        except FileNotFoundError:
            return ['Search terms not provided']

        if items > len(search_words):
            items = len(search_words)

        chosen_words = []
        while len(chosen_words) < items:
            word = random.choice(search_words)
            if word not in chosen_words:
                chosen_words.append(word)
        return chosen_words

    def log(self, step):
        '''self.log(message=Str)'''
        self.step = f'Func: {sys._getframe(1).f_code.co_name} >> {step}'

    def log_error(self, message, during='Unidentified error'):
        '''self.log_error(message=Str, during=Str)'''
        self.errors = False
        self.screenshots = True
        message = str(message).split('Stacktrace:')[0]
        msg = f'ERR during >> {during}\n\n{message}'
        print(msg)
        timestamp = datetime.now().strftime('%H%M%S')
        console_log = ''
        img_filename = None
        if self.driver != None:
            img_filename = self.take_screenshot(timestamp, '_ERR')
            path_to_img = os.path.join(self.logpath, img_filename)
            console_log = self.output_js_console()
        with open(os.path.join(self.logpath, f'{timestamp}_ERR.txt'), 'w', encoding='utf-8') as logfile:
            logfile.write(f'{msg}f\n\nConsole {"-" * 30}\n\n{console_log}')

        # Send email if test crashes
        if self.is_email:
            new_msg = MIMEMultipart()
            new_msg['From'] = SECRET.mail_from
            new_msg['To'] = SECRET.mail_to
            new_msg['Subject'] = self.testname
            new_msg.attach(MIMEText(f'\n\n{message}', 'plain'))

            if img_filename != None:
                payload = MIMEBase('application', 'octate-stream')
                with open(path_to_img, 'rb') as file:
                    payload.set_payload(file.read())
                    encoders.encode_base64(payload)
                    payload.add_header('Content-Disposition', 'attachement', filename=img_filename)
                    new_msg.attach(payload)
            text = new_msg.as_string()

            with smtplib.SMTP('smtp.gmail.com') as mailserver:
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
            message = f'*{self.testname} >>* {msg}'
            if img_filename != None:
                response = client.files_upload(
                    channels=SECRET.slack_channel,
                    initial_comment=message,
                    file=path_to_img
                )
            else:
                response = client.chat_postMessage(
                    channel=SECRET.slack_channel,
                    text=message
                )
            print(response.status_code)

    def log_results(self, name, url, logs, screenshots=True):
        '''
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
        '''
        self.screenshots = screenshots
        result = f'|{"=" * 90}\n| {name}\n| {url}\n'
        for log in logs:
            if not log:
                continue
            result += f'|{"-" * 90}\n'
            for key, value in log.items():
                if len(key) > 45:
                    row_name = f'{key[:40]}...'
                else:
                    row_name = key
                spacing = ' ' * (50 - len(row_name))
                result += f'| {row_name}{spacing}{value}\n'
        result += f'|{"=" * 90}\n'
        print(result)
        filename = f'{self.time}_out.txt'
        with open(os.path.join(self.logpath, filename), 'a', encoding='utf-8') as logfile:
            logfile.write(result)

    def new_test(self, screenshots=True):
        '''
        Set default values for test during each iteration, clear cache and cookies.
        It is meant to be run in 'for' loops at the beginning of each test.

        Example:
        - test.new_test()
        '''
        self.errors = True
        self.driver.delete_all_cookies()

    def output_js_console(self):
        '''self.output_js_console()'''
        pp = pprint.PrettyPrinter(indent=2)
        return pp.pformat([log for log in self.driver.get_log('browser')])

    def send_keys_slowly(self, element, text):
        '''self.send_keys_slowly(element=WebdriverObject, text=Str)'''
        for char in text:
            element.send_keys(char)
            self.sleep(1)

    def set_dev_theme(self, theme):
        '''self.set_dev_theme(theme=Str)'''
        dev_url = f'{self.home_url}/?preview_theme_id={theme}'
        response = requests.get(dev_url)
        if response.status_code == 200:
            print('DEV ENVIRONMENT ----------')
            self.driver.get(dev_url)
        self.sleep(5)

    def sleep(self, custom_delay=None):
        '''self.sleep(delay=Int)'''
        if custom_delay:
            time.sleep(custom_delay)
        else:
            time.sleep(self.default_delay)

    def take_screenshot(self, timestamp='', type=''):
        '''self.take_screenshot(timestamp=DatetimeObject, type=Str)'''
        if not self.screenshots:
            return
        if timestamp == '':
            timestamp = datetime.now().strftime('%H%M%S')
        method_name = sys._getframe(1).f_code.co_name
        method_name = re.sub('[^-a-zA-Z0-9_.() ]+', '', method_name)
        if not method_name:
            method_name = 'unknown'
        filename = f'{timestamp}{type}_{method_name}'
        png_img = os.path.join(self.logpath, f'{filename}.png')
        self.driver.save_screenshot(png_img)
        with Image.open(png_img) as rgba_img:
            jpg_img = os.path.join(self.logpath, f'{filename}.jpg')
            rgb_img = rgba_img.convert('RGB')
            rgb_img.save(jpg_img, optimize=True, quality=30)
        os.remove(png_img)
        return f'{filename}.jpg'


if __name__ == '__main__':
    pass