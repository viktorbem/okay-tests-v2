import functools
import random
from okay_tests import MainTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse


class OkayTest(MainTest):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def catch_error(f):
        @functools.wraps(f)
        def inner(self, *args, **kwargs):
            if self.errors:
                try:
                    return f(self, *args, **kwargs)
                except Exception as err:
                    self.log_error(message=err, during=self.step)
        return inner

    @catch_error
    def add_to_cart(self, screenshots=True):
        """
        Add current product to cart. Before running this method, you have to open some product in stock first, 
        eg. with open_product() method.

        Example:
        - test.add_to_cart()
        """
        self.screenshots = screenshots
        self.log("Get the name of the product")
        self.product_name = self.driver.find_element(By.CSS_SELECTOR, "h1.product_name").get_attribute("textContent")
        self.log(f"Add '{self.product_name}' to the cart")
        self.click(self.driver.find_element(By.NAME, "add"))

        self.sleep()
        self.log("Continue to the cart")
        try:
            self.click(self.driver.find_element(By.CSS_SELECTOR, "#cross-sell .button--add-to-cart"))
        except Exception as err:
            print("Product has no cross-sell ----------")
            self.sleep(10)
            if self.is_mobile:
                selector = ".mobile-icons .header-cart a"
            else:
                selector = ".header-cart a"

            self.click(self.driver.find_element(By.CSS_SELECTOR, selector))

        self.sleep()
        self.take_screenshot()

    @catch_error
    def check_services(self, services, screenshots=True):
        """
        Try to check all furniture services in cart. After all services are checked, take a screenshot. You have to
        provide a list of 'services' IDs that shoud be available for this category.

        Examples:
        - test.check_services(services=["40968686796951", "40968686829719"])
        - test.check_services(services=["40968686928023"])

        The 'services' argument is mandatory.
        """
        self.screenshots = screenshots
        for service in services:
            self.log(f"{service}: check if service is available")
            self.click(self.driver.find_element(By.XPATH, f"//input[@product-service-id={service}]"))
            self.sleep(5)
            
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.HOME)
        self.sleep()
        self.take_screenshot()

    @catch_error
    def choose_delivery(self, delivery, proceed=False, screenshots=True):
        """
        Choose delivery type defined in 'delivery' argument. You have to be in the 'shipping' step of checkout.

        Example:
        - test.choose_delivery(delivery='na moju adresu', proceed=True)

        The argument 'delivery' is mandatory and it should correspond to real delivery types on website.
        The argument 'proceed' is optional. If you set 'proceed' to 'True', test will proceed to next step.
        The default value of 'proceed' argument is 'False'.
        """
        self.screenshots = screenshots
        self.log("Get all possible delivery types")
        shipping_tabs = self.driver.find_elements(By.CSS_SELECTOR, ".checkout-shipping-tabs a")
        chosen_option = None
        for element in shipping_tabs:
            try:
                self.click(element)
            except Exception as err:
                print(f"'{element.text}' is not clickable ----------")
                continue

            shipping_options = self.driver.find_elements(By.CSS_SELECTOR, ".section--shipping-method .content-box__row")
            possible_options = [element for element in shipping_options if "table" in element.get_attribute("style")]

            self.log(f"Find delivery type that corresponds to '{delivery}'")
            for option in possible_options:
                
                delivery_option = option.find_element(By.CSS_SELECTOR, ".radio__label__primary")
                if delivery in delivery_option.get_attribute("data-shipping-method-label-title").lower():
                    chosen_option = option
                    break

            self.sleep()
            if chosen_option:
                break

        self.log(f"Click on the delivery type that corresponds to '{delivery}'")
        self.click(chosen_option)

        self.sleep()
        self.take_screenshot()

        if proceed:
            self.click(self.driver.find_element(By.ID, "continue_button"))
            self.sleep()

    @catch_error
    def choose_payment(self, payment, proceed=False, screenshots=True):
        """
        Choose payment type defined in 'payment' argument. You have to be in the 'payment' step of checkout.

        Example:
        test.choose_payment(payment='na moju adresu', proceed=True)

        The argument 'delivery' is mandatory and it should correspond to real delivery types on website.
        The argument 'proceed' is optional. If you set 'proceed' to 'True', test will proceed to next step.
        The default value of 'proceed' argument is 'False'.
        """
        self.screenshots = screenshots
        self.log("Get list of all possible payment options")
        payment_options = self.driver.find_elements(By.CSS_SELECTOR, ".section--payment-method fieldset .content-box__row")
        chosen_option = None
        self.log(f"Find payment type that corresponds to '{payment}'")
        for option in payment_options:
            if "secondary" in option.get_attribute("class"):
                continue
            payment_option = option.find_element(By.CSS_SELECTOR, ".radio__label__primary")
            if payment in payment_option.text.lower():
                chosen_option = option
                break
        
        self.sleep()
        self.log(f"Click on the payment type that corresponds to '{payment}'")
        self.click(chosen_option)
        
        self.sleep()
        self.take_screenshot()

        if proceed:
            self.click(self.driver.find_element(By.ID, "continue_button"))
            self.sleep()
            self.take_screenshot()

    @catch_error
    def confirm_order(self, screenshots=True):
        """
        Confirm if order was created by trying to click on some element in thank you page.

        Example:
        - test.confirm_order()
        """
        self.screenshots = screenshots
        self.log("Confirm if order was created")
        self.click(self.driver.find_element(By.CSS_SELECTOR, ".os-step__description a"))
        self.sleep()

    @catch_error
    def empty_cart(self, screenshots=True):
        """
        Open the cart and delete all items in it. This method won't raise any errors if there are no items in cart.

        Example:
        - test.empty_cart()
        """
        self.screenshots = screenshots
        self.log("Empty the cart")
        self.driver.get(f"{self.home_url}/cart")
        cart_is_empty = False
        while not cart_is_empty:
            self.sleep()
            try:
                self.click(self.driver.find_element(By.CSS_SELECTOR, ".cart__remove a"))
            except Exception as err:
                print("Cart is empty ----------")
                cart_is_empty = True
        
        self.sleep()

    @catch_error
    def goto_checkout(self, screenshots=True):
        """
        Proceed from the cart to the checkout. If you are currently not in cart, this method will open it for you first.
        It will also fill in all necessary order details if needed to proceed to the next step.

        Example:
        - test.goto_checkout()
        """
        self.screenshots = screenshots
        self.log("Proceed to the checkout")
        if "cart" not in self.driver.current_url:
            self.driver.get(f"{self.home_url}/cart")
            self.sleep()
        
        self.click(self.driver.find_element(By.NAME, "checkout"))

        self.sleep()
        self.log("Fill in all necessary details if needed")
        try:
            email = self.driver.find_element(By.ID, "checkout_email")
            email.send_keys("test.okay@okaycz.eu")
            firstname = self.driver.find_element_by_id("checkout_shipping_address_first_name")
            firstname.send_keys("test")
            surname = self.driver.find_element_by_id("checkout_shipping_address_last_name")
            surname.send_keys("test")
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

            self.log("Proceed to shipping form")
            self.click(self.driver.find_element(By.ID, "continue_button"))
        
        except Exception as err:
            print("Credentials already provided ----------")
        
        self.sleep()

    @catch_error
    def handle_gopay(self, screenshots=True):
        """
        Proceed through the payment gate until it is able to fill in credit card information,    
        then return back to the eshop to cancel order.

        Example:
        - test.handle_gopay()
        """
        self.screenshots = screenshots
        self.log("Wait for redirect to payment gate")
        self.sleep(20)
        self.take_screenshot()

        self.log("Choose payment by card")
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.sc-iCoGMd")
        for element in elements:
            if any(word in element.text.lower() for word in ["karta", "card"]):
                self.click(element)
                break
        
        self.log("Switch to iframe")
        self.sleep()
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

        self.log("Fill in card details")
        card_num = self.driver.find_element(By.NAME, "cardnumber")
        self.send_keys_slowly(card_num, "5555555555554444")
        self.sleep(2)
        expiration = self.driver.find_element(By.NAME, "exp-date")
        self.send_keys_slowly(expiration, "1230")
        self.sleep(2)
        cvc = self.driver.find_element(By.NAME, "cvc")
        self.send_keys_slowly(cvc, "123")

        self.sleep()
        self.take_screenshot()

        self.log("Switch back from iframe to main content")
        self.driver.switch_to.default_content()

        self.log("Close the payment plugin")
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.sc-eXuyPJ.grxFi")
        elements.extend(self.driver.find_elements(By.CSS_SELECTOR, "div.sc-gzcbmu.bENTHN"))
        element_found = False
        for element in elements:
            if "menu" in element.text.lower():
                element_found = True
                self.click(element)
                break
        if not element_found:
            raise Exception("Gopay: Unable to locate the 'menu' button.")
        
        self.sleep()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.sc-iCoGMd.hoarAx")
        element_found = False
        for element in elements:
            if any(word in element.text.lower() for word in ["zpět", "back"]):
                element_found = True
                element.click()
                break
        if not element_found:
            raise Exception("Gopay: Unable to locate the 'back' button.")
        
        self.log("Wait for redirect back to eshop")
        self.sleep(20)
                
    @catch_error
    def open_product(self, screenshots=True):
        """
        Look for the top bestseller in stock. If there is none, open the first product in collection.

        Example:
        - test.open_product()
        """
        self.screenshots = screenshots
        self.log("Get the list of the bestsellers")
        bestsellers = self.driver.find_elements(By.CSS_SELECTOR, ".flickity-slider div")

        self.log("Find the first product in stock and open it")
        test_product = None
        for item in bestsellers:
            try:
                item.find_element(By.CSS_SELECTOR, "span.in_stock")
                test_product = item.find_element(By.TAG_NAME, "a")
                break
            except Exception:
                continue

        if not test_product:
            self.log("There is no bestseller, choosing from other products")
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
    def open_random_menu_items(self, items, screenshots=True):
        """
        Get a list of all main menu items, randomly click as many as defined in argument and take screenshots of results.

        Example:
        - test.click_random_mainmenu_items(items=3)

        The argument 'items' is mandatory.
        This is going to click on 3 items in main menu.
        """
        self.screenshots = screenshots
        self.log(f"Click on {items} random items in main menu")
        clicked = []
        i = 0

        while i < items:
            self.sleep()

            should_open = True
            if self.is_mobile:
                menu_toggle = self.driver.find_element(By.CSS_SELECTOR, ".mobile-menu__toggle-button")
                if menu_toggle.get_attribute("data-show-mobile-menu") == "true":
                    should_open = False
            else:
                menu_toggle = self.driver.find_element(By.CSS_SELECTOR, ".header__open-menu")
                if "is-active" in menu_toggle.get_attribute("class"):
                    should_open = False
            
            if should_open:
                self.click(menu_toggle)
                self.sleep()

            menuitems = self.driver.find_elements(By.CSS_SELECTOR, ".nav-nested .nav-nested__link-parent")

            self.log(f"H{i}. choose random item from the menu")
            item = random.choice(menuitems)
            item_anchor = item.find_element(By.TAG_NAME, "a")
            item_url = item_anchor.get_attribute("href")

            if item_url not in clicked:
                self.log(f"{item_anchor.text} - click this item")
                clicked.append(item_url)
                self.click(item_anchor)
                if self.is_mobile:
                    self.sleep()
                    self.click(item.find_element(By.CSS_SELECTOR, ".nav-nested__forward"))

                self.sleep()
                self.take_screenshot()
                i += 1
            else:
                print(f"'{item_anchor.text}' already clicked ----------")

        self.sleep()

    @catch_error
    def open_random_footer_items(self, items, screenshots=True):
        """
        Get a list of all footer items, randomly click as many as defined in argument and take screenshots of results.

        Example:
        - test.click_random_footer_items(items=3)

        The argument 'items' is mandatory.
        This is going to click on 3 items in footer.
        """
        self.screenshots = screenshots
        self.log(f"Click on {items} random items in foooter")
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

            self.log(f"F{i}. choose random item from the footer")
            item = random.choice(footer_items)
            item_url = item.get_attribute("href")

            if item_url not in clicked and item_url.startswith(self.home_url):
                self.log(f"{item.text} - click this item")
                clicked.append(item_url)
                self.click(item)

                self.sleep()
                self.take_screenshot()
                i += 1
        
        self.sleep()

    @catch_error
    def open_specific_menu_item(self, text, screenshots=True):
        """
        Open an item in main menu items with link text provided as an argument.

        Example:
        - test.click_specific_mainmenu_item(text='Televízory')

        The argument 'text' is mandatory.
        """
        self.screenshots = screenshots
        if self.is_mobile:
            self.log("Open dropdown menu on mobile")
            self.click(self.driver.find_element(By.CSS_SELECTOR, ".mobile-menu__toggle-button"))
            self.sleep()

        self.log(f"Open category: {text}")
        item = self.driver.find_element(By.LINK_TEXT, text)
        self.click(item)

        if self.is_mobile:
            self.sleep()
            self.click(item.find_element(By.XPATH, "..").find_element(By.CSS_SELECTOR, ".nav-nested__forward"))
        
        self.sleep()

    @catch_error
    def open_specific_footer_item(self):
        """
        This method is yet to be done. Don't use it!
        """
        # TODO
        pass

    @catch_error
    def open_url(self, url, screenshots=True):
        """
        Open an URL defined as argument of this method.

        Example:
        - test.open_url(url='https://www.okay.cz/')

        The argument 'url' is mandatory.
        """
        self.screenshots = screenshots
        self.log(f"Open {url} in the browser")
        self.home_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}/"
        if self.theme != "":
            self.set_dev_theme(self.theme)
        self.driver.get(url)
        self.sleep()

    @catch_error
    def parse_delivery(self, screenshots=True):
        """
        Parse the list of all delivery options and return it as a dictionary.

        Example:
        - delivery = test.parse_delivery()
        """
        self.screenshots = screenshots
        self.sleep()
        self.log(f"Parse list of delivery options for '{self.product_name}'")
        self.take_screenshot()

        results = {}
        delivery_list = self.driver.find_elements(By.CSS_SELECTOR, ".section--shipping-method .content-box__row")
        for delivery in delivery_list:
            delivery_name_obj = delivery.find_element(By.CSS_SELECTOR, ".radio__label__primary")
            delivery_name = delivery_name_obj.get_attribute("data-shipping-method-label-title").strip()
            delivery_price_obj = delivery.find_element(By.CSS_SELECTOR, ".radio__label__accessory span")
            delivery_price = delivery_price_obj.get_attribute("innerHTML").replace("&nbsp;", " ").strip()
            results[delivery_name] = delivery_price
        return results

    @catch_error
    def parse_payment(self, screenshots=True):
        """
        Parse the list of all payment options and return it as a dictionary.

        Example:
        - payment = test.parse_payment()
        """
        self.screenshots = screenshots
        self.sleep()
        self.log(f"Parse list of payment options for '{self.product_name}'")
        self.take_screenshot()

        results = {}
        payment_list = self.driver.find_elements(By.CSS_SELECTOR, ".section--payment-method fieldset .content-box__row")
        for payment in payment_list:
            if "secondary" in payment.get_attribute("class"):
                continue
            payment_object = payment.find_element(By.CSS_SELECTOR, ".radio__label__primary")
            payment_data = payment_object.get_attribute("textContent").strip().split("\n")
            payment_name = payment_data[0].strip()
            if len(payment_data) > 1:
                payment_price = payment_data.pop().strip()
            else:
                payment_price = "-"
            results[payment_name] = payment_price
        return results

    @catch_error
    def search_for(self, text, screenshots=True):
        """
        Search a phrase defined by the 'text' argument.

        Example:
        - test.search_for(text='mobilný telefón')

        The argument 'text' is mandatory.
        """
        self.screenshots = screenshots
        self.log(f"Search for '{text}'")
        if self.is_mobile:
            self.log(f"Confirm search for '{text}' on mobile.")
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
            print(err)
            suggestion = self.driver.find_element(By.CSS_SELECTOR, ".boost-pfs-search-suggestion-item a")
        suggestion.click()

        self.sleep()
        self.take_screenshot()

    @catch_error
    def set_filter(self, name, value, screenshots=True):
        """
        Set a filter by name and value provided as arguments.

        Example:
        - test.set_filter(name='výrobcovia', value='lg')

        Both arguments are mandatory.
        """
        self.screenshots = screenshots
        if self.is_mobile:
            self.log("Open filter menu on mobile")
            wait = WebDriverWait(self.driver, 60)
            filter_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".boost-pfs-filter-tree-mobile-button button")))
            self.click(filter_btn)
            self.sleep()

            self.log(f"Open '{name}' filter on mobile")
            filter_options = self.driver.find_elements(By.CSS_SELECTOR, ".boost-pfs-filter-option-title button")
            is_found = False
            for item in filter_options:
                if str(name).lower() in item.text.lower():
                    self.click(item)
                    is_found = True
                    break
            if not is_found:
                raise Exception(f"The '{name}' filter was not found.")
            self.sleep()

        self.log(f"Set the '{name}' filter to '{value}'")
        filter = self.driver.find_elements(By.CSS_SELECTOR, ".boost-pfs-filter-button .boost-pfs-filter-option-value")
        is_found = False
        for item in filter:
            if str(value).lower() in item.text.lower():
                self.click(item)
                is_found = True
                break
        if not is_found:
            raise Exception(f"The '{value}' value of the '{name}' filter was not found.")
        self.sleep()

        if self.is_mobile:
            self.log(f"Accept the '{name}' filter on mobile")
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