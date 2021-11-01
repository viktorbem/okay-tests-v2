import random
import requests
import sys
from okay_tests import Maintest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OkaySK(Maintest):
    def __init__(self, theme="", **kwargs):
        super().__init__(**kwargs)
        self.home_url = "https://www.okay.sk"

        if theme != "":
            self.set_dev_theme(theme)

    def set_dev_theme(self, theme):
        dev_url = f"{self.home_url}/?preview_theme_id={theme}"
        response = requests.get(dev_url)
        if response.status_code == 200:
            print("DEV ENVIRONMENT ----------")
            url = dev_url
        self.driver.get(url)
        self.sleep(5)

    def catch_error(f):
        def inner(self, *args, **kwargs):
            try:
                f(self, *args, **kwargs)
            except Exception as err:
                self.log_error(message=err, during=self.step)
                self.abort()
                sys.exit()
        return inner

    @catch_error
    def add_to_cart(self):
        """
        Add current product to cart. Before running this method, you have to open some product in stock first, eg. with open_product() method.

        Example:
        - test.add_to_cart()
        """
        self.step = "Get the name of the product"
        product_name = self.driver.find_element(By.TAG_NAME, "h1").text
        self.step = f"Add '{product_name}' to the cart"
        self.click(self.driver.find_element(By.NAME, "add"))

        self.sleep()
        self.step = "Continue to the cart"
        try:
            self.click(self.driver.find_element(By.CSS, ".modal__overlay .button--add-to-cart"))
        except Exception as err:
            print("Product has no cross-sell ----------")
            self.sleep()
            if self.is_mobile:
                selector = ".mobile-icons .header-cart a"
            else:
                selector = ".header-cart a"

            self.click(self.driver.find_element(By.CSS_SELECTOR, selector))

        self.sleep()
        self.take_screenshot()

    @catch_error
    def choose_delivery(self, delivery, proceed=False):
        """
        Choose delivery type defined in 'delivery' argument. You have to be in the 'shipping' step of checkout.

        Example:
        test.choose_delivery(delivery='na moju adresu', proceed=True)

        The argument 'delivery' is mandatory and it should correspond to real delivery types on website.
        The argument 'proceed' is optional. If you set 'proceed' to 'True', test will proceed to next step.
        The default value of 'proceed' argument is 'False'.
        """
        self.step = "Get all possible delivery types"
        shipping_tabs = self.driver.find_elements(By.CSS_SELECTOR, ".checkout-shipping-tabs a")
        chosen_option = None
        for element in shipping_tabs:
            self.click(element)

            shipping_options = self.driver.find_elements(By.CSS_SELECTOR, ".section--shipping-method .content-box__row")
            possible_options = [element for element in shipping_options if "table" in element.get_attribute("style")]

            self.step = f"Find delivery type that corresponds to '{delivery}'"
            for option in possible_options:
                
                delivery_option = option.find_element(By.CSS_SELECTOR, ".radio__label__primary")
                if delivery in delivery_option.get_attribute("data-shipping-method-label-title").lower():
                    chosen_option = option
                    break

            self.sleep()
            if chosen_option:
                break

        self.step = f"Click on the delivery type that corresponds to '{delivery}'"
        self.click(chosen_option)

        self.sleep()
        self.take_screenshot()

        if proceed:
            self.click(self.driver.find_element(By.ID, "continue_button"))
            self.sleep()

    @catch_error
    def choose_payment(self, payment, proceed=False):
        """
        Choose payment type defined in 'payment' argument. You have to be in the 'payment' step of checkout.

        Example:
        test.choose_payment(payment='na moju adresu', proceed=True)

        The argument 'delivery' is mandatory and it should correspond to real delivery types on website.
        The argument 'proceed' is optional. If you set 'proceed' to 'True', test will proceed to next step.
        The default value of 'proceed' argument is 'False'.
        """
        self.step = "Get list of all possible payment options"
        payment_options = self.driver.find_elements(By.CSS_SELECTOR, ".section--payment-method fieldset .content-box__row")
        chosen_option = None
        self.step = f"Find payment type that corresponds to '{payment}'"
        for option in payment_options:
            if "secondary" in option.get_attribute("class"):
                continue
            payment_option = option.find_element(By.CSS_SELECTOR, ".radio__label__primary")
            if payment in payment_option.text.lower():
                chosen_option = option
                break
        
        self.sleep()
        self.step = f"Click on the payment type that corresponds to '{payment}'"
        self.click(chosen_option)
        
        self.sleep()
        self.take_screenshot()

        if proceed:
            self.click(self.driver.find_element(By.ID, "continue_button"))
            self.sleep()
            
    @catch_error
    def goto_checkout(self):
        """
        Proceed from the cart to the checkout. If you are currently not in cart, this method will open it for you first.
        It will also fill in all necessary order details if needed to proceed to the next step.

        Example:
        - test.goto_checkout()
        """
        self.step = "Proceed to the checkout"
        if "cart" not in self.driver.current_url:
            self.driver.get(f"{self.home_url}/cart")
            self.sleep()
        
        self.click(self.driver.find_element(By.NAME, "checkout"))

        self.sleep()
        self.step = "Fill in all necessary details if needed"
        try:
            email = self.driver.find_element(By.ID, "checkout_email")
            email.send_keys("test.okay@okaycz.eu")
            firstname = self.driver.find_element_by_id("checkout_shipping_address_first_name")
            firstname.send_keys("test")
            surname = self.driver.find_element_by_id("checkout_shipping_address_last_name")
            surname.send_keys("selenium")
            street = self.driver.find_element_by_id("checkout_shipping_address_address1")
            street.send_keys("Testovaci 123")
            zipnr = self.driver.find_element_by_id("checkout_shipping_address_zip")
            zipnr.send_keys("83300")
            city = self.driver.find_element_by_id("checkout_shipping_address_city")
            city.send_keys("Bratislava")
            phonenr = self.driver.find_element_by_id("checkout_shipping_address_phone")
            phonenr.send_keys("608123123")

            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.HOME)

            self.sleep()
            self.take_screenshot()

            self.step = "Proceed to shipping form"
            self.click(self.driver.find_element(By.ID, "continue_button"))
        
        except Exception as err:
            print(err)
        
        self.sleep()

    @catch_error
    def open_product(self):
        """
        Looks for the top bestseller in stock. If there is none, opens the first product in collection.

        Example:
        - test.open_product()
        """
        self.step = "Get the list of the bestsellers"
        bestsellers = self.driver.find_elements(By.CSS_SELECTOR, ".flickity-slider div")

        self.step = "Find the first product in stock and open it"
        test_product = None
        for item in bestsellers:
            try:
                item.find_element(By.CSS_SELECTOR, "span.in_stock")
                test_product = item.find_element(By.TAG_NAME, "a")
                break
            except Exception:
                continue

        if not test_product:
            self.step = "There is no bestseller, choosing from other products"
            products = self.driver.find_elements(By.CSS_SELECTOR, ".collection-matrix div")
            for item in products:
                try:
                    item.find_element(By.CSS_SELECTOR, "span.in_stock")
                    test_product = item.find_element(By.TAG_NAME, "a")
                    break
                except Exception:
                    continue

        self.click(test_product)

        self.sleep()
        self.take_screenshot()

    @catch_error
    def open_random_menu_items(self, items):
        """
        Get a list of all main menu items, randomly click as many as defined in argument and take screenshots of results.

        Example:
        - test.click_random_mainmenu_items(items=3)

        The argument 'items' is mandatory.
        This is going to click on 3 items in main menu.
        """

        self.step = f"Click on {items} random items in main menu"
        clicked = []
        i = 0

        if self.is_mobile:
            selector = ".mobile-menu__toggle-button"
        else:
            selector = ".header__open-menu"

        while i < items:
            self.sleep()
            self.click(self.driver.find_element(By.CSS_SELECTOR, selector))

            self.sleep()
            menuitems = self.driver.find_elements(By.CSS_SELECTOR, ".nav-nested .nav-nested__link-parent")

            self.step = f"H{i}. choose random item from the menu"
            item = random.choice(menuitems)
            item_anchor = item.find_element(By.TAG_NAME, "a")
            item_url = item_anchor.get_attribute("href")

            if item_url not in clicked:
                self.step = f"{item_anchor.text} - click this item"
                clicked.append(item_url)
                self.click(item_anchor)
                if self.is_mobile:
                    self.sleep()
                    self.click(item.find_element(By.CSS_SELECTOR, "nav-nested__forward"))

                self.sleep()
                self.take_screenshot()
                i += 1

        self.sleep()

    @catch_error
    def open_random_footer_items(self, items):
        """
        Get a list of all footer items, randomly click as many as defined in argument and take screenshots of results.

        Example:
        - test.click_random_footer_items(items=3)

        The argument 'items' is mandatory.
        This is going to click on 3 items in footer.
        """

        self.step = f"Click on {items} random items in foooter"
        clicked = []
        i = 0

        while i < items:
            self.sleep()

            if self.is_mobile:
                parent_items = self.driver.find_elements(By.CSS_SELECTOR, "footer .footer__menu")
                parent = random.choice(parent_items)
                self.click(parent)
                footer_items = parent.find_elements(By.CSS_SELECTOR, ".footer__menu-link a")
            else:
                footer_items = self.driver.find_elements(By.CSS_SELECTOR, "footer a")

            self.step = f"F{i}. choose random item from the footer"
            item = random.choice(footer_items)
            item_url = item.get_attribute("href")

            if item_url not in clicked and item_url.startswith(self.home_url):
                self.step = f"{item.text} - click this item"
                clicked.append(item_url)
                self.click(item)

                self.sleep()
                self.take_screenshot()
                i += 1
        
        self.sleep()

    @catch_error
    def open_specific_menu_item(self, text):
        """
        Open an item in main menu items with link text provided as an argument.

        Example:
        - test.click_specific_mainmenu_item(text='Televízory')

        The argument 'text' is mandatory.
        """
        if self.is_mobile:
            self.step = "Open dropdown menu on mobile"
            self.click(self.driver.find_element(By.CSS_SELECTOR, ".mobile-menu__toggle-button"))
            self.sleep()

        self.step = f"Open category: {text}"
        item = self.driver.find_element(By.LINK_TEXT, text)
        self.click(item)

        if self.is_mobile:
            self.sleep()
            self.click(item.find_element(By.XPATH, "..").find_element(By.CSS_SELECTOR, ".nav-nested__forward"))
        
        self.sleep()

    @catch_error
    def open_specific_footer_item(self):
        # TODO
        pass

    @catch_error
    def open_url(self, url):
        """
        Open an URL defined as argument of this method.

        Example:
        - test.open_url(url='https://www.okay.sk/')

        The argument 'url' is mandatory.
        """
        self.step = f"Open {url} in the browser"
        self.driver.get(url)
        self.sleep()

    @catch_error
    def search_for(self, text):
        """
        Search a phrase defined by the 'text' argument.

        Example:
        - test.search_for(text='mobilný telefón')

        The argument 'text' is mandatory.
        """
        self.step = f"Search for '{text}'"
        if self.is_mobile:
            self.step = "Click search button on mobile."
            self.click(self.driver.find_element(By.CSS_SELECTOR, ".mobile-icons a"))

            self.sleep()
            search_bar = self.driver.find_element(By.ID, "boost-pfs-search-box-mobile")
        else:
            search_bar = self.driver.find_element(By.NAME, "q")
        
        search_bar.clear()
        search_bar.send_keys(text)

        self.sleep()
        self.take_screenshot()

        self.sleep()
        try:
            suggestion = self.driver.find_element(By.CSS_SELECTOR, ".boost-pfs-search-suggestion-item b")
        except Exception as err:
            suggestion = self.driver.find_element(By.CSS_SELECTOR, ".boost-pfs-search-suggestion-item")
        self.click(suggestion)

        self.sleep()
        self.take_screenshot()

    @catch_error
    def set_filter(self, name, value):
        """
        Sets a filter by name and value provided as arguments.

        Example:
        - test.set_filter(name='výrobcovia', value='lg')

        Both arguments are mandatory.
        """

        if self.is_mobile:
            self.step = "Open filter menu on mobile"
            wait = WebDriverWait(self.driver, 60)
            filter_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".boost-pfs-filter-tree-mobile-button button")))
            self.click(filter_btn)
            self.sleep()

            self.step = f"Open '{name}' filter on mobile"
            filter_options = self.driver.find_elements(By.CSS_SELECTOR, ".boost-pfs-filter-option-title button")
            for item in filter_options:
                if str(name).lower() in item.text.lower():
                    self.click(item)
                    break
            self.sleep()

        self.step = f"Set the '{name}' filter to '{value}'"        
        filter = self.driver.find_elements(By.CSS_SELECTOR, ".boost-pfs-filter-button .boost-pfs-filter-option-value")
        for item in filter:
            if str(value).lower() in item.text.lower():
                self.click(item)
                break
        self.sleep()

        if self.is_mobile:
            self.step = f"Accept the '{name}' filter on mobile"
            self.click(self.driver.find_element(By.CSS_SELECTOR, ".boost-pfs-filter-back-btn"))
            self.sleep()
            self.take_screenshot()
            self.click(self.driver.find_element(By.CSS_SELECTOR, ".boost-pfs-filter-show-result"))
        else:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.HOME)
            self.sleep()
            self.take_screenshot()
        self.sleep()


if __name__ == "__main__":
    pass