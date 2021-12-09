from okay_tests import OkayTest


## OKAY.SK MENU DESKTOP

test = OkayTest(name="okaysk_menu", delay=3)
test.open_url(url="https://www.okay.sk/")
test.open_random_menu_items(3)
test.open_random_footer_items(3)
test.abort()


## OKAY.SK MENU MOBILE

test = OkayTest(name="okaysk_menu_mobile", is_mobile=True, delay=3)
test.open_url(url="https://www.okay.sk/")
test.open_random_menu_items(3)
test.open_random_footer_items(3)
test.abort()


## OKAY.SK FILTERS DESKTOP

test = OkayTest(name="okaysk_filters", delay=3)
test.open_url(url="https://www.okay.sk/")
test.open_specific_menu_item(text="Televízory")
test.set_filter(name="výrobcovia", value="lg")
test.set_filter(name="uhlopriečka", value="55")
test.abort()


## OKAY.SK FILTERS MOBILE

test = OkayTest(name="okaysk_filters_mobile", is_mobile=True, delay=3)
test.open_url(url="https://www.okay.sk/")
test.open_specific_menu_item(text="Postele")
test.set_filter(name="rozmery", value="180 x 200")
test.set_filter(name="úložný priestor", value="ano")
test.abort()


## OKAY.SK SEARCH DESKTOP

test = OkayTest(name="okaysk_search")
test.open_url(url="https://www.okay.sk/")
test.search_for(text="mobilny telefon")
test.search_for(text="vankúš")
test.search_for(text="predajne")
test.search_for(text="iphone v akcii")
test.search_for(text="nintendo")
test.search_for(text="ako vybrať")
test.abort()


## OKAY.SK SEARCH MOBILE

test = OkayTest(name="okaysk_search_mobile", is_mobile=True, delay=3)
test.open_url(url="https://www.okay.sk/")
test.search_for(text="mobilny telefon")
test.search_for(text="bratislava")
test.search_for(text="splátky")
test.search_for(text="doprava")
test.abort()


## OKAY.SK UNFINISHED ORDER DESKTOP

test = OkayTest(name="okaysk_unfinished_order", delay=3)
test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="bankový prevod", proceed=False)
test.abort()


## OKAY.SK UNFINISHED ORDER MOBILE

test = OkayTest(name="okaysk_unfinished_order_mobile", is_mobile=True, delay=3)
test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="bankový prevod", proceed=False)
test.abort()


## OKAY.SK FINISHED COD ORDER

test = OkayTest(name="okaysk_finished_cod_order", delay=3)
test.open_url(url="https://www.okay.sk/collections/alkalicke-baterie?sort=price-ascending")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="dobierka", proceed=True)
test.confirm_order()
test.abort()


## OKAY.SK PAYMENT GATE

test = OkayTest(name="okaysk_payment_gate", delay=3)
test.open_url(url="https://www.okay.sk/products/baterie-varta-energy-aaa-4ks")
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
            "40968686829719", # Montaz sedaciho nabytku a posteli
        ],
    },
    {
        "name": "POSTELE",
        "url": "https://www.okay.sk/collections/postele",
        "services": [
            "40968686796951", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            "40968686829719", # Montaz sedaciho nabytku a posteli
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
    }
]

test = OkayTest(name="okaysk_furniture_services", delay=3)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product()
    test.add_to_cart()
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

test = OkayTest(name="okaysk_delivery_options_electro", delay=3)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product()
    test.add_to_cart()
    test.goto_checkout()
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na moju adresu", proceed=True)
    payment = test.parse_payment()
    test.choose_payment(payment="dobierka", proceed=False)
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

test = OkayTest(name="okaysk_delivery_options_furniture", delay=3)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category["url"])
    test.open_product()
    test.add_to_cart()
    test.goto_checkout()
    delivery = test.parse_delivery()
    test.choose_delivery(delivery="na moju adresu", proceed=True)
    payment = test.parse_payment()
    test.choose_payment(payment="dobierka", proceed=False)
    test.log_results(
        name=category["name"],
        url=category["url"],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()
