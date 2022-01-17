import time
from okay_tests import OkayTest

start = time.perf_counter()


## OKAY.CZ MENU DESKTOP

test = OkayTest(name="okaycz_menu")
test.open_url(url="https://www.okay.cz/")
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## OKAY.CZ MENU MOBILE

test = OkayTest(name="okaycz_menu_mobile", is_mobile=True)
test.open_url(url="https://www.okay.cz/")
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## OKAY.CZ FILTERS DESKTOP

test = OkayTest(name="okaycz_filters")
test.open_url(url="https://www.okay.cz/")
test.open_specific_menu_item(text="Televize")
test.set_filter(name="výrobci", value="lg")
test.set_filter(name="úhlopříčka", value="55")
test.abort()


## OKAY.CZ FILTERS MOBILE

test = OkayTest(name="okaycz_filters_mobile", is_mobile=True)
test.open_url(url="https://www.okay.cz/")
test.open_specific_menu_item(text="Postele")
test.set_filter(name="rozměry", value="180 x 200")
test.set_filter(name="úložný prostor", value="ano")
test.abort()


## OKAY.CZ SEARCH DESKTOP

test = OkayTest(name="okaycz_search")
test.open_url(url="https://www.okay.cz/")
words = test.get_random_words(items=5)
for word in words:
    test.search_for(text=word)
test.abort()


## OKAY.CZ SEARCH MOBILE

test = OkayTest(name="okaycz_search_mobile", is_mobile=True)
test.open_url(url="https://www.okay.cz/")
words = test.get_random_words(items=5)
for word in words:
    test.search_for(text=word)
test.abort()


## OKAY.CZ UNFINISHED ORDER DESKTOP

test = OkayTest(name="okaycz_unfinished_order")
test.open_url(url="https://www.okay.cz/collections/mobilni-telefony-3")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="bankovní převod", proceed=False)
test.abort()


## OKAY.CZ UNFINISHED ORDER MOBILE

test = OkayTest(name="okaycz_unfinished_order_mobile", is_mobile=True)
test.open_url(url="https://www.okay.cz/collections/mobilni-telefony-3")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="bankovní převod", proceed=False)
test.abort()


## OKAY.CZ FINISHED COD ORDER

test = OkayTest(name="okaycz_finished_cod_order")
test.open_url(url="https://www.okay.cz/collections/alkalicke-baterie?pf_p_ceny=59.00%3A180.00")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="dobírka", proceed=True)
test.confirm_order()
test.abort()


## OKAY.CZ PAYMENT GATE

test = OkayTest(name="okaycz_payment_gate")
test.open_url(url="https://www.okay.cz/collections/alkalicke-baterie?pf_p_ceny=59.00%3A180.00")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na mou adresu", proceed=True)
test.choose_payment(payment="karta", proceed=True)
# test.handle_gopay()
# test.empty_cart()
test.abort()


## OKAY.CZ FURNITURE SERVICES

CATEGORIES = [
    {
        "name": "SEDACKY",
        "url": "https://www.okay.cz/collections/rozkladaci-rohove-sedaci-soupravy",
        "services": [
            "39660571918378", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            # "39660571951146", # Montaz sedaciho nabytku a posteli
        ],
    },
    {
        "name": "POSTELE",
        "url": "https://www.okay.cz/collections/postele",
        "services": [
            "39660571918378", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            # "39660571951146", # Montaz sedaciho nabytku a posteli
        ],
    },
    {
        "name": "KUCHYNSKE LINKY ROHOVE",
        "url": "https://www.okay.cz/collections/rohove-4",
        "services": [
            "39660572016682", # Montaz kuchyne (rohova)
            "39660572147754", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
            "39660572180522", # Likvidace dreveneho nabytku a kuchyni
        ],
    },
    {
        "name": "KUCHYNSKE LINKY ROVNE",
        "url": "https://www.okay.cz/collections/rovne-3",
        "services": [
            "39660572082218", # Montaz kuchyne (rovna)
            "39660572147754", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
            "39660572180522", # Likvidace dreveneho nabytku a kuchyni
        ],
    }
]

test = OkayTest(name="okaycz_furniture_services")
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.check_services(services=category["services"])
    test.empty_cart()
test.abort()


## OKAY.CZ DELIVERY OPTIONS ELECTRO

CATEGORIES = [
    {
        "name": "(8) Do 3 kg",
        "url": "https://www.okay.cz/collections/mobilni-telefony-3?pf_st_expedice=true",
    },
    {
        "name": "(1) Do 30 kg",
        "url": "https://www.okay.cz/collections/kuchynske-roboty?pf_st_expedice=true",
    },
    {
        "name": "(2) Do 50 kg",
        "url": "https://www.okay.cz/collections/volne-stojici-mikrovlnne-trouby?pf_st_expedice=true",
    },
    {
        "name": "(3) Nadrozměrný balík",
        "url": "https://www.okay.cz/collections/tv-s-uhloprickou-40-az-43-101-az-109-cm?pf_st_expedice=true",
    },
    {
        "name": "(4) 1/2 Paleta",
        "url": "https://www.okay.cz/collections/samostatne-vestavne-trouby?pf_st_expedice=true",
    },
    {
        "name": "(5) Paleta",
        "url": "https://www.okay.cz/collections/kombinovane-lednice?pf_st_expedice=true",
    },
    {
        "name": "(7) Dvoupaleta",
        "url": "https://www.okay.cz/collections/americke-lednice?pf_st_expedice=true",
    }
]

test = OkayTest(name="okaycz_delivery_options_electro")
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.goto_checkout(screenshots=False)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na mou adresu", proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment="dobírka", proceed=False, screenshots=False)
    test.log_results(
        name=category["name"],
        url=category["url"],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## OKAY.CZ DELIVERY OPTIONS FURNITURE

CATEGORIES = [
    {
        "name": "(8) Do 3 kg",
        "url": "https://www.okay.cz/collections/polstarky-k-sedacim-soupravam",
    },
    {
        "name": "(1) Do 30 kg",
        "url": "https://www.okay.cz/collections/barove-zidle-2",
    },
    {
        "name": "(2) Do 50 kg",
        "url": "https://www.okay.cz/collections/rosty-2",
    },
    {
        "name": "(3) Nadrozměrný balík",
        "url": "https://www.okay.cz/collections/matrace-90x200",
    },
    {
        "name": "(4) 1/2 Paleta",
        "url": "https://www.okay.cz/collections/valendy-2",
    },
    {
        "name": "(5) Paleta",
        "url": "https://www.okay.cz/collections/kresla-2",
    },
    {
        "name": "(7) Dvoupaleta - kuchyne",
        "url": "https://www.okay.cz/collections/rovne-3",
    },
    {
        "name": "(7) Dvoupaleta - sedacka",
        "url": "https://www.okay.cz/collections/rohove-sedaci-soupravy",
    }
]

test = OkayTest(name="okaycz_delivery_options_furniture")
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.goto_checkout(screenshots=False)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na mou adresu", proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment="převod", proceed=False, screenshots=False)
    test.log_results(
        name=category["name"],
        url=category["url"],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## OKAY.CZ SALESFORCE FORMS CHECK

FORMS = [
    {
        "url": "https://www.okay.cz/pages/kontaktni-formular-95",
        "fields": [
            {
                "id": "storeifyInput_fcb5bc50-10d3-4126-a193-cb0749b5f2f6",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_bca19a60-ee00-4b02-9e9c-641cf4c2a176",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_b7ae96e0-468e-4cf5-9d0c-01af528ff1ec",
                "value": "Message filled by Selenium"
            }
        ]
    },
    {
        "url": "https://www.okay.cz/pages/kontaktni-formular-219",
        "fields": [
            {
                "id": "storeifyInput_fcb5bc50-10d3-4126-a193-cb0749b5f2f6",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_bca19a60-ee00-4b02-9e9c-641cf4c2a176",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_b7ae96e0-468e-4cf5-9d0c-01af528ff1ec",
                "value": "Message filled by Selenium"
            }
        ]
    },
        {
        "url": "https://www.okay.cz/pages/kontaktni-formular-reklamace",
        "fields": [
            {
                "id": "storeifyInput_fcb5bc50-10d3-4126-a193-cb0749b5f2f6",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_bca19a60-ee00-4b02-9e9c-641cf4c2a176",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_b7ae96e0-468e-4cf5-9d0c-01af528ff1ec",
                "value": "Message filled by Selenium"
            }
        ]
    }
]

test = OkayTest(name="okaycz_salesforce_forms")
for form in FORMS:
    test.new_test()
    test.open_url(url=form["url"])
    test.fill_form_fields(fields=form["fields"], proceed=False)
test.abort()

test = OkayTest(name="okaycz_salesforce_forms_mobile", is_mobile=True)
for form in FORMS:
    test.new_test()
    test.open_url(url=form["url"])
    test.fill_form_fields(fields=form["fields"], proceed=False)
test.abort()


end = time.perf_counter() - start
print(f"Finished in {end:.2f} s")
