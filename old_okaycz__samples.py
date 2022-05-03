from okay_tests import LegacyTest
from __user import EMAIL, PASSWORD


# OLD OKAY.CZ STORE LOGGED IN UNFINISHED ORDER

CATEGORIES = [
    {
        "url": "https://old.okay.cz/televize/?dostupnost=skladem"
    },
    {
        "url": "https://old.okay.cz/rozkladaci-sedaci-soupravy/?dostupnost=skladem"
    }
]

test = LegacyTest(name="old_okaycz_store_logged_in")
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.login_user(username=EMAIL, password=PASSWORD)
    test.open_product()
    test.add_to_cart()
    test.goto_shipment()
    test.choose_delivery_and_payment(delivery="na mou adresu", payment="převod", proceed=True)
    test.fill_address()
test.abort()