import time
from okay_tests import JenaTest

start = time.perf_counter()


## JENA MENU DESKTOP

test = JenaTest(name="jena_menu")
test.open_url(url="https://www.jena-nabytek.cz/")
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## JENA MENU MOBILE

test = JenaTest(name="jena_menu_mobile", is_mobile=True)
test.open_url(url="https://www.jena-nabytek.cz/")
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## JENA FILTERS DESKTOP

test = JenaTest(name="jena_filters")
test.open_url(url="https://www.jena-nabytek.cz/")
test.open_specific_menu_item(text="Sedačky")
test.set_filter(name="styl", value="moderní")
test.set_filter(name="materiál", value="látka")
test.abort()


## JENA FILTERS MOBILE

test = JenaTest(name="jena_filters_mobile", is_mobile=True)
test.open_url(url="https://www.jena-nabytek.cz/")
test.open_specific_menu_item(text="Postele")
test.set_filter(name="rozměr", value="180 x 200")
test.set_filter(name="úložný prostor", value="ano")
test.abort()


## JENA SEARCH DESKTOP

test = JenaTest(name="jena_search")
test.open_url(url="https://www.jena-nabytek.cz/")
test.search_for(text="postele boxspring")
test.search_for(text="polštáře")
test.search_for(text="ostrava")
test.search_for(text="splátky")
test.search_for(text="doprava")
test.abort()


## JENA SEARCH MOBILE

test = JenaTest(name="jena_search_mobile", is_mobile=True)
test.open_url(url="https://www.jena-nabytek.cz/")
test.search_for(text="postele boxspring")
test.search_for(text="polštáře")
test.search_for(text="ostrava")
test.search_for(text="splátky")
test.search_for(text="doprava")
test.abort()


## JENA UNFINISHED ORDER DESKTOP

test = JenaTest(name="jena_unfinished_order")
test.open_url(url="https://www.jena-nabytek.cz/collections/postele")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="gopay", proceed=False)
test.abort()


## JENA UNFINISHED ORDER MOBILE

test = JenaTest(name="jena_unfinished_order_mobile", is_mobile=True)
test.open_url(url="https://www.jena-nabytek.cz/collections/postele")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="gopay", proceed=False)
test.abort()


# ## JENA FINISHED ORDER

# test = JenaTest(name="jena_finished_order")
# test.open_url(url="https://www.jena-nabytek.cz/collections/dekoracni-polstare?pf_p_cena=99%3A1000")
# test.open_product()
# test.add_to_cart()
# test.goto_checkout()
# test.choose_delivery(delivery="na mou adresu", proceed=True)
# test.choose_payment(payment="bankovní převod", proceed=True)
# test.confirm_order()
# test.abort()


## JENA PAYMENT GATE

test = JenaTest(name="jena_payment_gate")
test.open_url(url="https://www.jena-nabytek.cz/collections/dekoracni-polstare?pf_p_cena=99%3A1000")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="gopay", proceed=True)
# test.handle_gopay()
# test.empty_cart()
test.abort()


## JENA FURNITURE SERVICES

CATEGORIES = [
    {
        "name": "SEDACKY",
        "url": "https://www.jena-nabytek.cz/collections/sedacky",
        "services": [
            "38218900930712", # Odvoz a ekologicka likvidace nabytku
        ],
    },
    {
        "name": "POSTELE",
        "url": "https://www.jena-nabytek.cz/collections/postele",
        "services": [
            "38218900930712", # Odvoz a ekologicka likvidace nabytku
        ],
    },
    {
        "name": "KUCHYNSKE LINKY ROHOVE",
        "url": "https://www.jena-nabytek.cz/collections/rohove-kuchyne",
        "services": [
            "38218900996248", # Montaz kuchyne (rohova)
            "39248582279320", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
        ],
    },
    {
        "name": "KUCHYNSKE LINKY ROVNE",
        "url": "https://www.jena-nabytek.cz/collections/rovne-kuchyne",
        "services": [
            "39248505634968", # Montaz kuchyne (rovna)
            "39248582279320", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
        ],
    }
]

test = JenaTest(name="jena_furniture_services")
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.check_services(services=category["services"])
    test.empty_cart()
test.abort()


## JENA DELIVERY OPTIONS FURNITURE

CATEGORIES = [
    {
        "name": "(8) Do 3 kg",
        "url": "https://www.jena-nabytek.cz/collections/dekoracni-polstare",
    },
    {
        "name": "(1) Do 30 kg",
        "url": "https://www.jena-nabytek.cz/collections/barove-zidle",
    },
    {
        "name": "(2) Do 50 kg",
        "url": "https://www.jena-nabytek.cz/collections/rosty",
    },
    {
        "name": "(3) Nadrozměrný balík",
        "url": "https://www.jena-nabytek.cz/collections/matrace-90x200",
    },
    {
        "name": "(4) 1/2 Paleta",
        "url": "https://www.jena-nabytek.cz/collections/valendy",
    },
    {
        "name": "(5) Paleta",
        "url": "https://www.jena-nabytek.cz/collections/kresla",
    },
    {
        "name": "(7) Dvoupaleta",
        "url": "https://www.jena-nabytek.cz/collections/rohove-sedacky",
    }
]

test = JenaTest(name="jena_delivery_options_furniture")
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.goto_checkout(screenshots=False)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na mou adresu", proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment="gopay", proceed=False, screenshots=False)
    test.log_results(
        name=category["name"],
        url=category["url"],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## JENA SALESFORCE FORMS CHECK

FORMS = [
    {
        "url": "https://www.jena-nabytek.cz/pages/kontaktujte-nas-moje-platba",
        "fields": [
            {
                "id": "storeifyInput_5581b8ef-35db-4cf4-8ffd-008188d67aaa",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_e4eb4879-c3df-437a-bd7c-e782087ff672",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_ac1a85cc-9830-404b-8427-81f13990cfc6",
                "value": "Message filled by Selenium"
            }
        ]
    },
    {
        "url": "https://www.jena-nabytek.cz/pages/kontaktujte-nas-27282",
        "fields": [
            {
                "id": "storeifyInput_5581b8ef-35db-4cf4-8ffd-008188d67aaa",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_e4eb4879-c3df-437a-bd7c-e782087ff672",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_ac1a85cc-9830-404b-8427-81f13990cfc6",
                "value": "Message filled by Selenium"
            }
        ]
    },
        {
        "url": "https://www.jena-nabytek.cz/pages/formular-pro-reklamacni-rizeni-nabytku",
        "fields": [
            {
                "id": "storeifyInput_5581b8ef-35db-4cf4-8ffd-008188d67aaa",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_e4eb4879-c3df-437a-bd7c-e782087ff672",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_ac1a85cc-9830-404b-8427-81f13990cfc6",
                "value": "Message filled by Selenium"
            }
        ]
    }
]

test = JenaTest(name="jena_salesforce_forms")
for form in FORMS:
    test.new_test()
    test.open_url(url=form["url"])
    test.fill_form_fields(fields=form["fields"], proceed=False)
test.abort()

test = JenaTest(name="jena_salesforce_forms_mobile", is_mobile=True)
for form in FORMS:
    test.new_test()
    test.open_url(url=form["url"])
    test.fill_form_fields(fields=form["fields"], proceed=False)
test.abort()


end = time.perf_counter() - start
print(f"Finished in {end:.2f} s")
