from okay_tests import MainTest
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


class LegacyTest(MainTest):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def catch_error(f):
        return MainTest.catch_error(f)

    @catch_error
    def add_to_cart(self):
        """
        Add current product to cart. Before running this method, you have to open some product in stock first, 
        eg. with open_product() method.

        Example:
        - test.add_to_cart()
        """
        self.log("Add this item to the cart")
        self.click(self.driver.find_element(By.CSS_SELECTOR, ".add-basket .btn-wrap__button span"))

        self.log("Continue to the cart")
        self.sleep()

        try:
            self.click(self.driver.find_element(By.CSS_SELECTOR, ".js-prebasket-step-1 .js-prebasket-continue-button-anchor"))
        except Exception as err:
            print("Product has no cross-sell...\n")

        self.sleep()
        self.click(self.driver.find_element(By.CSS_SELECTOR, ".box-prebasket .btn.go-to-basket"))

        self.sleep()
        self.take_screenshot()

    @catch_error
    def choose_delivery_and_payment(self, delivery, payment, proceed=True):
        """
        Choose delivery type defined in 'delivery' argument and payment type defined in 'payment' argument.
        You have to be in the 'shipping' step of checkout.

        Example:
        - test.choose_delivery_and_payment(delivery="na mou adresu", payment="převod", proceed=True)

        The arguments 'delivery' and 'payment' are mandatory and they should correspond to real types on website.
        The argument 'proceed' is optional. If you set 'proceed' to 'True', test will proceed to next step.
        The default value of 'proceed' argument is 'False'.
        """
        self.log(f"Choose '{delivery}' delivery option")
        deliveries = self.driver.find_elements(By.CSS_SELECTOR, ".transport_envelope li")
        for item in deliveries:
            if delivery.lower() in item.text.lower():
                self.click(item.find_element(By.CSS_SELECTOR, "input[type='radio']"))
                break

        self.log(f"Choose '{payment}' payment option")
        self.sleep()

        try:
            self.click(self.driver.find_element(By.ID, "payment-sloz-all-before"))
            self.sleep()
        except Exception as err:
            print("No down payment needed...\n")

        boxes = self.driver.find_elements(By.CSS_SELECTOR, ".box-yellow")

        for box in boxes:
            payments = box.find_elements(By.CSS_SELECTOR, " li")
            for item in payments:
                if payment.lower() in item.text.lower():
                    self.click(item.find_element(By.CSS_SELECTOR, "input[type='radio']"))
                    break

        self.sleep()
        self.take_screenshot()

        if proceed:
            self.log("Proceed to checkout")
            self.click(self.driver.find_element(By.CSS_SELECTOR, "button[name='next-step-3']"))
            self.sleep()

    @catch_error
    def fill_address(self):
        """
        Fill in all the necessary order details needed to proceed to finish the order.

        Example:
        - test.fill_address()
        """
        self.log("Fill all the necessary details")

        email = self.driver.find_element(By.ID, "email")
        email.send_keys("test.okay@okaycz.eu")
        self.sleep(1)

        firstname = self.driver.find_element(By.ID, "jmeno")
        firstname.send_keys("test")
        self.sleep(1)

        lastname = self.driver.find_element(By.ID, "prijmeni")
        lastname.send_keys("test")
        self.sleep(1)

        phonenr = self.driver.find_element(By.ID, "telefon")
        phonenr.send_keys("608123456")
        self.sleep(1)

        street = self.driver.find_element(By.ID, "ulice")
        street.send_keys("Testovaci 123")
        self.sleep(1)

        city = self.driver.find_element(By.ID, "mesto")
        city.send_keys("Brno")
        self.sleep(1)

        zipnr = self.driver.find_element(By.ID, "bill_zip")
        zipnr.send_keys("60200")
        self.sleep(1)

        self.sleep()
        self.take_screenshot()

    @catch_error
    def goto_shipment(self):
        """
        Proceed from the cart to the checkout. If you are currently not in cart, this method will open it for you first.

        Example:
        - test.goto_checkout()
        """
        self.log("Proceed to shipment")
        if "kosik" not in self.driver.current_url:
            self.driver.get(f"{self.home_url}kosik")
            self.sleep()

        self.click(self.driver.find_element(By.CSS_SELECTOR, "form[name='order'] button[name='next-step-2']"))

        self.sleep()
        self.take_screenshot()

    @catch_error
    def login_user(self, username, password):
        """
        Log in as user specified in 'username' and 'password' arguments.

        Example:
        - test.login_user(username="test@okay.cz", password="testpassword")

        Both arguments are mandatory.
        """
        self.log(f"Log in as '{username}'")
        self.click(self.driver.find_element(By.CSS_SELECTOR, ".box-user-box__link"))
        self.sleep()

        self.log("Fill in the credentials")
        user = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='E-mail']")
        self.send_keys_slowly(user, username)

        userpass = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Heslo']")
        self.send_keys_slowly(userpass, password)

        self.log("Click the login button")
        self.sleep()
        self.click(self.driver.find_element(By.ID, "submit_button"))

        self.sleep()
        self.take_screenshot()

    @catch_error
    def open_product(self):
        """
        Go to the detail of the first product in collection.

        Example:
        - test.open_product()
        """
        self.log("Get first item in stock")
        self.click(self.driver.find_element(By.CSS_SELECTOR, ".js-gtm-product-link"))

        self.sleep()
        self.take_screenshot()

    @catch_error
    def open_url(self, url):
        """
        Open an URL defined as argument of this method.

        Example:
        - test.open_url(url='https://old.okay.cz/')

        The argument 'url' is mandatory.
        """
        self.log(f"Open {url} in the browser")
        self.last_url = url
        self.home_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}/"
        if self.shop_password != "":
            self.bypass_password(self.home_url)
        if self.theme != "":
            self.set_dev_theme(self.theme)
        self.driver.get(url)
        self.sleep()
