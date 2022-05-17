import time
from okay_tests import OkayTest

start = time.perf_counter()

THEME = ""

## OKAY.SK MENU DESKTOP

test = OkayTest(name="okaysk_menu", theme=THEME)
test.open_url(url="https://www.okay.sk/")
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## OKAY.SK MENU MOBILE

test = OkayTest(name="okaysk_menu_mobile", is_mobile=True, theme=THEME)
test.open_url(url="https://www.okay.sk/")
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## OKAY.SK FILTERS DESKTOP

test = OkayTest(name="okaysk_filters", theme=THEME)
test.open_url(url="https://www.okay.sk/")
test.open_specific_menu_item(text="Televízory")
test.set_filter(name="výrobcovia", value="lg")
test.set_filter(name="uhlopriečka", value="55")
test.abort()


## OKAY.SK FILTERS MOBILE

test = OkayTest(name="okaysk_filters_mobile", is_mobile=True, theme=THEME)
test.open_url(url="https://www.okay.sk/")
test.open_specific_menu_item(text="Postele")
test.set_filter(name="rozmery", value="180 x 200")
test.set_filter(name="úložný priestor", value="ano")
test.abort()


## OKAY.SK SEARCH DESKTOP

test = OkayTest(name="okaysk_search", theme=THEME, is_slack=False)
test.open_url(url="https://www.okay.sk/")
words = test.get_random_words(items=5)
for word in words:
    test.search_for(text=word)
test.abort()


## OKAY.SK SEARCH MOBILE

test = OkayTest(name="okaysk_search_mobile", is_mobile=True, theme=THEME, is_slack=False)
test.open_url(url="https://www.okay.sk/")
words = test.get_random_words(items=5)
for word in words:
    test.search_for(text=word)
test.abort()


## OKAY.SK UNFINISHED ORDER DESKTOP

test = OkayTest(name="okaysk_unfinished_order", theme=THEME)
test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="bankový prevod", proceed=False)
test.abort()


## OKAY.SK UNFINISHED ORDER MOBILE

test = OkayTest(name="okaysk_unfinished_order_mobile", is_mobile=True, theme=THEME)
test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="bankový prevod", proceed=False)
test.abort()


## OKAY.SK FINISHED COD ORDER

test = OkayTest(name="okaysk_finished_cod_order", theme=THEME)
test.open_url(url="https://www.okay.sk/collections/alkalicke-baterie?pf_p_ceny=2.28%3A5.28")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="packeta", proceed=False, screenshots=False)
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="dobierka", proceed=True)
test.confirm_order()
test.abort()


## OKAY.SK PAYMENT GATE

test = OkayTest(name="okaysk_payment_gate", theme=THEME)
test.open_url(url="https://www.okay.sk/collections/vankuse-a-prikryvky?pf_p_cena=3.96%3A40.00&pf_st_expedicia=true")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="karta", proceed=True)
test.handle_gopay()
test.empty_cart()
test.abort()


## OKAY.SK FURNITURE SERVICES

CATEGORIES = [
    {
        "name": "SEDACKY",
        "url": "https://www.okay.sk/collections/rohove-sedacky-rozkladacie",
        "services": [
            "40968686796951", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            "40968686829719", # Montaz sedacieho nabytku a posteli
            "40968686928023", # Demontaz a likvidacia dreveneho nabytku a kuchyn
        ],
    },
    {
        "name": "POSTELE",
        "url": "https://www.okay.sk/collections/postele",
        "services": [
            "40968686796951", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            "40968686928023", # Demontáž a likvidácia dreveného nábytku a kuchýň
            "41050674692247", # Likvidácia dreveného nábytku a kuchýň
            "42026198696087", # Montáž dreveného nábytku
        ],
    },
    {
        "name": "KUCHYNSKE LINKY ROHOVE",
        "url": "https://www.okay.sk/collections/rohove-5",
        "services": [
            "40968686862487", # Montaz kuchyne (rohova)
            "40968686928023", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
            "41050674692247", # Likvidace dreveneho nabytku a kuchyni
        ],
    },
    {
        "name": "KUCHYNSKE LINKY ROVNE",
        "url": "https://www.okay.sk/collections/rovne-kuchynske",
        "services": [
            "40968686895255", # Montaz kuchyne (rovna)
            "40968686928023", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
            "41050674692247", # Likvidace dreveneho nabytku a kuchyni
        ],
    },
    {
        "name": "DREVO LEHKA MONTAZ",
        "url": "https://www.okay.sk/collections/drevene-postele",
        "services": [
            "40968686796951", # Odvoz a ekologická likvidácia sedacieho nábytku a postelí
            "40968686928023", # Demontáž a likvidácia dreveného nábytku a kuchýň
            "41050674692247", # Likvidácia dreveného nábytku a kuchýň
            "42026198696087", # Montáž dreveného nábytku
        ],
    },
    {
        "name": "DREVO STREDNI MONTAZ",
        "url": "https://www.okay.sk/collections/obyvacie-steny",
        "services": [
            "40968686928023", # Demontáž a likvidácia dreveného nábytku a kuchýň
            "41050674692247", # Likvidácia dreveného nábytku a kuchýň
            "42026219012247", # Montáž dreveného nábytku
        ],
    }
]

test = OkayTest(name="okaysk_furniture_services", theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=True)
    test.add_to_cart(screenshots=True)
    test.check_services(services=category["services"])
    test.empty_cart()
test.abort()


## OKAY.SK DELIVERY OPTIONS ELECTRO

CATEGORIES = [
    {
        "name": "(8) Do 3 kg",
        "url": "https://www.okay.sk/collections/mobilne-telefony-4?pf_st_expedicia=true",
    },
    {
        "name": "(1) Do 30 kg",
        "url": "https://www.okay.sk/collections/kuchynske-roboty?pf_st_expedicia=true",
    },
    {
        "name": "(2) Do 50 kg",
        "url": "https://www.okay.sk/collections/mikrovlnne-rury-a-mini-rury?pf_st_expedicia=true",
    },
    {
        "name": "(3) Nadrozměrný balík",
        "url": "https://www.okay.sk/collections/tv-s-uhloprieckou-40-az-43-101-az-109-cm?pf_st_expedicia=true",
    },
    {
        "name": "(4) 1/2 Paleta",
        "url": "https://www.okay.sk/collections/vstavne-rury-2?pf_st_expedicia=true",
    },
    {
        "name": "(5) Paleta",
        "url": "https://www.okay.sk/collections/biele-chladnicky-s-mraznickou?pf_st_expedicia=true",
    },
    {
        "name": "(7) Dvoupaleta",
        "url": "https://www.okay.sk/collections/americke-chladnicky?pf_st_expedicia=true",
    }
]

test = OkayTest(name="okaysk_delivery_options_electro", theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=True)
    test.add_to_cart(screenshots=True)
    test.goto_checkout(screenshots=True)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na moju adresu", proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment="dobierka", proceed=False, screenshots=False)
    test.log_results(
        name=category["name"],
        url=category["url"],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## OKAY.SK DELIVERY OPTIONS FURNITURE

CATEGORIES = [
    {
        "name": "(8) Do 3 kg",
        "url": "https://www.okay.sk/collections/vankusiky-k-sedackam",
    },
    {
        "name": "(1) Do 30 kg",
        "url": "https://www.okay.sk/collections/barove-stolicky-2",
    },
    {
        "name": "(2) Do 50 kg",
        "url": "https://www.okay.sk/collections/rosty-6",
    },
    {
        "name": "(3) Nadrozměrný balík",
        "url": "https://www.okay.sk/collections/matrace-90x200",
    },
    {
        "name": "(4) 1/2 Paleta",
        "url": "https://www.okay.sk/collections/valandy-2",
    },
    {
        "name": "(5) Paleta",
        "url": "https://www.okay.sk/collections/kresla-2",
    },
    {
        "name": "(7) Dvoupaleta - kuchyne",
        "url": "https://www.okay.sk/collections/rovne-kuchynske",
    },
    {
        "name": "(7) Dvoupaleta - sedacka",
        "url": "https://www.okay.sk/collections/rohove-o",
    }
]

test = OkayTest(name="okaysk_delivery_options_furniture", theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=True)
    test.add_to_cart(screenshots=True)
    test.goto_checkout(screenshots=True)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na moju adresu", proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment="prevod", proceed=False, screenshots=False)
    test.log_results(
        name=category["name"],
        url=category["url"],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## OKAY.SK SALESFORCE FORMS CHECK

FORMS = [
    {
        "url": "https://www.okay.sk/pages/kontaktny-formular-95",
        "fields": [
            {
                "id": "storeifyInput_dd2694a1ab83",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_80d9e047-cb39-48bd-bf96-873076f441ee",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_2e349aba-9533-4c31-994f-a7b25ec6bdbc",
                "value": "Message filled by Selenium"
            }
        ]
    },
    {
        "url": "https://www.okay.sk/pages/kontaktny-formular-125",
        "fields": [
            {
                "id": "storeifyInput_dd2694a1ab83",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_80d9e047-cb39-48bd-bf96-873076f441ee",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_2e349aba-9533-4c31-994f-a7b25ec6bdbc",
                "value": "Message filled by Selenium"
            }
        ]
    },
        {
        "url": "https://www.okay.sk/pages/kontaktny-formular-reklamacia",
        "fields": [
            {
                "id": "storeifyInput_dd2694a1ab83",
                "value": "Jan"
            },
            {
                "id": "storeifyInput_80d9e047-cb39-48bd-bf96-873076f441ee",
                "value": "Novak"
            },
            {
                "id": "storeifyInput_2e349aba-9533-4c31-994f-a7b25ec6bdbc",
                "value": "Message filled by Selenium"
            }
        ]
    }
]

test = OkayTest(name="okaysk_salesforce_forms", theme=THEME)
for form in FORMS:
    test.new_test()
    test.open_url(url=form["url"])
    test.fill_form_fields(fields=form["fields"], proceed=False)
test.abort()

test = OkayTest(name="okaysk_salesforce_forms_mobile", is_mobile=True, theme=THEME)
for form in FORMS:
    test.new_test()
    test.open_url(url=form["url"])
    test.fill_form_fields(fields=form["fields"], proceed=False)
test.abort()


## OKAY.SK PRICE CHECK FURNITURE

CATEGORIES = [
    "https://www.okay.sk/collections/sedacie-supravy?pf_st_expedicia=true",
    "https://www.okay.sk/collections/pracky-a-susicky?pf_st_expedicia=true"
]

test = OkayTest(name="okaysk_price_check_furniture", theme=THEME)
for cat_url in CATEGORIES:
    test.new_test()
    test.open_url(url=cat_url)
    products = test.find_elements(selector=".collection-matrix__wrapper .product-wrap")
    was_prices = test.find_elements(selector=".collection-matrix__wrapper .product-thumbnail__was-price")
    if len(products) > 0 and len(was_prices) == 0:
        test.log_error(
            message=f"There are no crossed prices available on {test.last_url}", 
            during="Check crossed prices on page"
        )
test.abort()


# OKAY.SK FURNITURE ON ORDER

test = OkayTest(name="okaysk_furniture_on_order", theme=THEME)
page = 1
found_product = None
while not found_product:
    test.open_url(url=f"https://www.okay.sk/collections/sedacie-supravy?page={page}")
    products = test.find_elements(selector=".collection-matrix__wrapper .product-wrap")
    for product in products:
        if len(test.find_child_elements(product, ".tag.on_order")) > 0:
            found_product = test.find_child_element(product, ".product-thumbnail__title")
            break
    page += 1
test.click(found_product, delay=True)
test.add_to_cart()
test.abort()


# OKAY.SK INSIA INSURANCES

CATEGORIES = [
    {
        "name": "TELEVIZE",
        "url": "https://www.okay.sk/collections/televizory",
        "insurances": [
            "7519182127255", # Asistencie elektro Axa
            "7519183175831", # Poistenie náhodného poškodenia a odcudzenia na 2 roky
            "7519181963415", # Predĺžená záruka na 5 rokov
        ],
    },
    {
        "name": "LEDNICE",
        "url": "https://www.okay.sk/collections/chladnicky",
        "insurances": [
            "7519182127255", # Asistencie elektro Axa
            "7519183175831", # Poistenie náhodného poškodenia a odcudzenia na 2 roky
            "7519181963415", # Predĺžená záruka na 5 rokov
        ],
    },
    {
        "name": "SMARTPHONY",
        "url": "https://www.okay.sk/collections/chytre-telefony",
        "insurances": [
            "7519182127255", # Asistencie elektro Axa
            "7519183405207", # Poistenie náhodného poškodenia a odcudzenia na 2 roky
            "7519180456087", # Predĺžená záruka na 3 roky
        ],
    },
    {
        "name": "POSTELE",
        "url": "https://www.okay.sk/collections/postele",
        "insurances": [
            "7519180587159", # Asistencie Home exclusive Axa
        ],
    },
    {
        "name": "SEDACKY",
        "url": "https://www.okay.sk/collections/rozkladacie-sedacky-v-tvare-u",
        "insurances": [
            "7519180587159", # Asistencie Home exclusive Axa
        ],
    }
]

test = OkayTest(name="okaysk_insia_insurances", theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.check_insurances(insurances=category["insurances"])
    test.empty_cart()
test.abort()


## OKAY.SK STORE WIDGET

test = OkayTest(name="okaysk_store_widget", theme=THEME)
test.open_url(url="https://www.okay.sk/")
test.open_random_menu_items(items=1, screenshots=False)
test.open_product(screenshots=False)
test.add_to_cart(screenshots=False)
test.goto_checkout(screenshots=False)
test.choose_delivery(delivery="osobný odber", proceed=False, screenshots=False)
test.select_pickup_point(proceed=True)
test.choose_payment(payment="prevod", proceed=False)
test.abort()


end = time.perf_counter() - start
print(f"Finished in {end:.2f} s")
