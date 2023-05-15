import time
from okay_tests import OkayTest

start = time.perf_counter()

THEME = ''

## OKAY.CZ MENU DESKTOP

test = OkayTest(name='okaycz_menu', theme=THEME)
test.open_url(url='https://www.okay.cz/')
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## OKAY.CZ MENU MOBILE

test = OkayTest(name='okaycz_menu_mobile', is_mobile=True, theme=THEME)
test.open_url(url='https://www.okay.cz/')
test.open_random_menu_items(items=3)
test.open_random_footer_items(items=3)
test.abort()


## OKAY.CZ FILTERS DESKTOP

test = OkayTest(name='okaycz_filters', theme=THEME)
test.open_url(url='https://www.okay.cz/')
test.open_specific_menu_item(text='Televize')
test.set_filter(name='výrobci', value='lg')
test.set_filter(name='technologie', value='led')
test.abort()


## OKAY.CZ FILTERS MOBILE

test = OkayTest(name='okaycz_filters_mobile', is_mobile=True, theme=THEME)
test.open_url(url='https://www.okay.cz/')
test.open_specific_menu_item(text='Postele')
test.set_filter(name='rozměry', value='180 x 200')
test.set_filter(name='úložný prostor', value='ano')
test.abort()


## OKAY.CZ SEARCH DESKTOP

test = OkayTest(name='okaycz_search', theme=THEME, is_slack=False)
test.open_url(url='https://www.okay.cz/')
words = test.get_random_words(items=5)
for word in words:
    test.search_for(text=word)
test.abort()


## OKAY.CZ SEARCH MOBILE

test = OkayTest(name='okaycz_search_mobile', is_mobile=True, theme=THEME, is_slack=False)
test.open_url(url='https://www.okay.cz/')
words = test.get_random_words(items=5)
for word in words:
    test.search_for(text=word)
test.abort()


## OKAY.CZ UNFINISHED ORDER DESKTOP

test = OkayTest(name='okaycz_unfinished_order', theme=THEME)
test.open_url(url='https://www.okay.cz/collections/mobilni-telefony-3')
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery='na mou adresu', exclude='mastercard', proceed=True)
test.choose_payment(payment='platba bankou', proceed=False)
test.abort()


## OKAY.CZ UNFINISHED ORDER MOBILE

test = OkayTest(name='okaycz_unfinished_order_mobile', is_mobile=True, theme=THEME)
test.open_url(url='https://www.okay.cz/collections/mobilni-telefony-3')
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery='na mou adresu', exclude='mastercard', proceed=True)
test.choose_payment(payment='platba bankou', proceed=False)
test.abort()


## OKAY.CZ FINISHED COD ORDER

test = OkayTest(name='okaycz_finished_cod_order', theme=THEME)
test.open_url(url='https://www.okay.cz/collections/baterie?pf_p_ceny=59.00%3A180.00')
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery='zásilkovna', proceed=False, screenshots=False)
test.choose_delivery(delivery='na mou adresu', exclude='mastercard', proceed=True)
test.choose_payment(payment='dobírka', proceed=True)
test.confirm_order()
test.abort()


## OKAY.CZ PAYMENT GATE

test = OkayTest(name='okaycz_payment_gate', theme=THEME)
test.open_url(url='https://www.okay.cz/collections/polstare-a-prikryvky?pf_p_cena=99.00%3A999.00&pf_st_expedice=true')
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery='na mou adresu', exclude='mastercard', proceed=True)
test.choose_payment(payment='karta', proceed=True)
test.handle_gopay()
test.empty_cart()
test.abort()


## OKAY.CZ SELLER OFFER

# test = OkayTest(name='okaycz_seller_offer', theme=THEME)
# test.open_url(url='https://www.okay.cz/pages/prihlaseni-prodejce')
# test.login_seller()
# test.open_random_menu_items(items=1, screenshots=False)
# test.open_product()
# test.add_to_cart(screenshots=False)
# test.send_offer(email='petr.stroh@online.okay.cz')
# test.abort()


## OKAY.CZ FURNITURE SERVICES

CATEGORIES = [
    {
        'name': 'SEDACKY',
        'url': 'https://www.okay.cz/collections/rozkladaci-rohove-sedaci-soupravy',
        'services': [
            '39660571918378', # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            '39660571951146', # Montaz sedaciho nabytku
            '39660572147754', # Demontáž a likvidace dřevěného nábytku a kuchyní
        ],
    },
    {
        'name': 'POSTELE',
        'url': 'https://www.okay.cz/collections/calounene',
        'services': [
            '39660571918378', # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
            '39660572147754', # Demontáž a likvidace dřevěného nábytku a kuchyní
            # '39660572180522', # Likvidace dřevěného nábytku a kuchyní
            '40081972756522', # Montáž dřevěného nábytku
        ],
    },
    {
        'name': 'KUCHYNSKE LINKY ROHOVE',
        'url': 'https://www.okay.cz/collections/rohove-4',
        'services': [
            '39660572016682', # Montaz kuchyne (rohova)
            '39660572147754', # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
            '39660572180522', # Likvidace dreveneho nabytku a kuchyni
        ],
    },
    {
        'name': 'KUCHYNSKE LINKY ROVNE',
        'url': 'https://www.okay.cz/collections/rovne-3',
        'services': [
            '39660572082218', # Montaz kuchyne (rovna)
            '39660572147754', # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
            '39660572180522', # Likvidace dreveneho nabytku a kuchyni
        ],
    },
    {
        'name': 'DREVO LEHKA MONTAZ',
        'url': 'https://www.okay.cz/collections/drevene-3',
        'services': [
            '39660571918378', # Odvoz a ekologická likvidace sedacího nábytku a postelí
            '39660572147754', # Demontáž a likvidace dřevěného nábytku a kuchyní
            # '39660572180522', # Likvidace dřevěného nábytku a kuchyní
            '40081972756522', # Montáž dřevěného nábytku
        ],
    },
    {
        'name': 'DREVO STREDNI MONTAZ',
        'url': 'https://www.okay.cz/collections/loznicove-komplety',
        'services': [
            '39660572147754', # Demontáž a likvidace dřevěného nábytku a kuchyní
            '39660572180522', # Likvidace dřevěného nábytku a kuchyní
            '40081973837866', # Montáž dřevěného nábytku
        ],
    }
]

test = OkayTest(name='okaycz_furniture_services', theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category['url'])
    test.open_product(screenshots=True)
    test.add_to_cart(screenshots=True)
    test.check_services(services=category['services'])
    test.empty_cart()
test.abort()


## OKAY.CZ DELIVERY OPTIONS ELECTRO

CATEGORIES = [
    {
        'name': '(8) Do 3 kg',
        'url': 'https://www.okay.cz/collections/mobilni-telefony-3?pf_st_expedice=true',
    },
    {
        'name': '(1) Do 30 kg',
        'url': 'https://www.okay.cz/collections/kuchynske-roboty?pf_st_expedice=true',
    },
    {
        'name': '(2) Do 50 kg',
        'url': 'https://www.okay.cz/collections/volne-stojici-mikrovlnne-trouby?pf_st_expedice=true',
    },
    {
        'name': '(3) Nadrozměrný balík',
        'url': 'https://www.okay.cz/collections/tv-s-uhloprickou-40-az-43-101-az-109-cm?pf_st_expedice=true',
    },
    {
        'name': '(4) 1/2 Paleta',
        'url': 'https://www.okay.cz/collections/samostatne-vestavne-trouby?pf_st_expedice=true',
    },
    {
        'name': '(5) Paleta',
        'url': 'https://www.okay.cz/collections/kombinovane-lednice?pf_st_expedice=true',
    },
    {
        'name': '(7) Dvoupaleta',
        'url': 'https://www.okay.cz/collections/americke-lednice?pf_st_expedice=true',
    }
]

test = OkayTest(name='okaycz_delivery_options_electro', theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category['url'])
    test.open_product(screenshots=True)
    test.add_to_cart(screenshots=True)
    test.goto_checkout(screenshots=True)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery='na mou adresu', exclude='mastercard', proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment='dobírka', proceed=False, screenshots=False)
    test.log_results(
        name=category['name'],
        url=category['url'],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## OKAY.CZ DELIVERY OPTIONS FURNITURE

CATEGORIES = [
    {
        'name': '(8) Do 3 kg',
        'url': 'https://www.okay.cz/collections/polstarky-k-sedacim-soupravam',
    },
    {
        'name': '(1) Do 30 kg',
        'url': 'https://www.okay.cz/collections/barove-zidle-2',
    },
    {
        'name': '(2) Do 50 kg',
        'url': 'https://www.okay.cz/collections/rosty-2',
    },
    {
        'name': '(3) Nadrozměrný balík',
        'url': 'https://www.okay.cz/collections/matrace-90x200',
    },
    {
        'name': '(4) 1/2 Paleta',
        'url': 'https://www.okay.cz/collections/valendy-2',
    },
    {
        'name': '(5) Paleta',
        'url': 'https://www.okay.cz/collections/kresla-2',
    },
    {
        'name': '(7) Dvoupaleta - kuchyne',
        'url': 'https://www.okay.cz/collections/rovne-3',
    },
    {
        'name': '(7) Dvoupaleta - sedacka',
        'url': 'https://www.okay.cz/collections/rohove-sedaci-soupravy',
    }
]

test = OkayTest(name='okaycz_delivery_options_furniture', theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category['url'])
    test.open_product(screenshots=True)
    test.add_to_cart(screenshots=True)
    test.goto_checkout(screenshots=True)
    delivery = test.parse_delivery()
    test.choose_delivery(delivery='na mou adresu', exclude='mastercard', proceed=True, screenshots=False)
    payment = test.parse_payment()
    test.choose_payment(payment='platba bankou', proceed=False, screenshots=False)
    test.log_results(
        name=category['name'],
        url=category['url'],
        logs=[delivery, payment]
    )
    test.empty_cart()
test.abort()


## OKAY.CZ SALESFORCE FORMS CHECK

FORMS = [
    {
        'url': 'https://www.okay.cz/pages/kontaktni-formular-95',
        'fields': [
            {
                'id': 'storeifyInput_fcb5bc50-10d3-4126-a193-cb0749b5f2f6',
                'value': 'Jan'
            },
            {
                'id': 'storeifyInput_bca19a60-ee00-4b02-9e9c-641cf4c2a176',
                'value': 'Novak'
            },
            {
                'id': 'storeifyInput_b7ae96e0-468e-4cf5-9d0c-01af528ff1ec',
                'value': 'Message filled by Selenium'
            }
        ]
    },
    {
        'url': 'https://www.okay.cz/pages/kontaktni-formular-219',
        'fields': [
            {
                'id': 'storeifyInput_fcb5bc50-10d3-4126-a193-cb0749b5f2f6',
                'value': 'Jan'
            },
            {
                'id': 'storeifyInput_bca19a60-ee00-4b02-9e9c-641cf4c2a176',
                'value': 'Novak'
            },
            {
                'id': 'storeifyInput_b7ae96e0-468e-4cf5-9d0c-01af528ff1ec',
                'value': 'Message filled by Selenium'
            }
        ]
    },
        {
        'url': 'https://www.okay.cz/pages/kontaktni-formular-reklamace',
        'fields': [
            {
                'id': 'storeifyInput_fcb5bc50-10d3-4126-a193-cb0749b5f2f6',
                'value': 'Jan'
            },
            {
                'id': 'storeifyInput_bca19a60-ee00-4b02-9e9c-641cf4c2a176',
                'value': 'Novak'
            },
            {
                'id': 'storeifyInput_b7ae96e0-468e-4cf5-9d0c-01af528ff1ec',
                'value': 'Message filled by Selenium'
            }
        ]
    }
]

test = OkayTest(name='okaycz_salesforce_forms', theme=THEME)
for form in FORMS:
    test.new_test()
    test.open_url(url=form['url'])
    test.fill_form_fields(fields=form['fields'], proceed=False)
test.abort()

test = OkayTest(name='okaycz_salesforce_forms_mobile', is_mobile=True, theme=THEME)
for form in FORMS:
    test.new_test()
    test.open_url(url=form['url'])
    test.fill_form_fields(fields=form['fields'], proceed=False)
test.abort()


## OKAY.CZ PRICE CHECK FURNITURE

CATEGORIES = [
    'https://www.okay.cz/collections/sedaci-soupravy?pf_st_expedice=true',
    'https://www.okay.cz/collections/pracky-a-susicky?pf_st_expedice=true'
]

test = OkayTest(name='okaycz_price_check_furniture', theme=THEME)
for cat_url in CATEGORIES:
    test.new_test()
    test.open_url(url=cat_url)
    products = test.find_elements(selector='.collection-matrix__wrapper .product-wrap')
    was_prices = test.find_elements(selector='.collection-matrix__wrapper .product-thumbnail__was-price')
    if len(products) > 0 and len(was_prices) == 0:
        test.log_error(
            message=f'There are no crossed prices available on {test.last_url}', 
            during='Check crossed prices on page'
        )
test.abort()


# OKAY.CZ FURNITURE ON ORDER

test = OkayTest(name='okaycz_furniture_on_order', theme=THEME)
page = 5
found_product = None
while not found_product:
    test.open_url(url=f'https://www.okay.cz/collections/sedaci-soupravy?page={page}')
    products = test.find_elements(selector='.collection-matrix__wrapper .product-wrap')
    for product in products:
        if len(test.find_child_elements(product, '.tag.on_order')) > 0:
            found_product = test.find_child_element(product, '.product-thumbnail__title')
            break
    page += 1
test.click(found_product, delay=True)
test.add_to_cart()
test.abort()


# OKAY.CZ INSIA INSURANCES

CATEGORIES = [
    {
        'name': 'TELEVIZE',
        'url': 'https://www.okay.cz/collections/televize',
        'insurances': [
            '6797255966762', # Prodloužení záruky na 5 let
            '6797255901226', # Pojištění náhodného poškození a krádeže na 2 roky
            '6797255573546', # Asistence elektro Axa
        ],
    },
    {
        'name': 'LEDNICE',
        'url': 'https://www.okay.cz/collections/lednice-2',
        'insurances': [
            '6797255966762', # Prodloužení záruky na 5 let
            '6797255835690', # Pojištění náhodného poškození a krádeže na 2 roky
            '6797255573546', # Asistence elektro Axa
        ],
    },
    {
        'name': 'SMARTPHONY',
        'url': 'https://www.okay.cz/collections/chytre-telefony',
        'insurances': [
            '6797256065066', # Prodloužení záruky na 3 roky
            '6797256097834', # Pojištění náhodného poškození a krádeže na 2 roky
            '6797255573546', # Asistence elektro Axa
        ],
    },
    {
        'name': 'POSTELE',
        'url': 'https://www.okay.cz/collections/postele?pf_p_cena=10000%3A39999',
        'insurances': [
            '6797256130602', # Pojištění nábytku TOP na 2 roky
            '6797256196138', # Asistence Home exclusive Axa
        ],
    },
    {
        'name': 'SEDACKY',
        'url': 'https://www.okay.cz/collections/sedaci-soupravy-do-u-rozkladaci',
        'insurances': [
            '6797256130602', # Pojištění nábytku TOP na 2 roky
            '6797256196138', # Asistence Home exclusive Axa
        ],
    }
]

test = OkayTest(name='okaycz_insia_insurances', theme=THEME)
for category in CATEGORIES:
    test.new_test()
    test.open_url(url=category['url'])
    test.open_product(screenshots=False)
    test.add_to_cart(screenshots=False)
    test.check_insurances(insurances=category['insurances'])
    test.empty_cart()
test.abort()


## OKAY.CZ STORE WIDGET

test = OkayTest(name='okaycz_store_widget', theme=THEME)
test.open_url(url='https://www.okay.cz/')
test.open_random_menu_items(items=1, limit=5, screenshots=False)
test.open_product(screenshots=False)
test.add_to_cart(screenshots=False)
test.goto_checkout(screenshots=False)
test.choose_delivery(delivery='osobní odběr', proceed=False, screenshots=False)
test.select_pickup_point(proceed=True)
test.choose_payment(payment='platba bankou', proceed=False)
test.abort()

end = time.perf_counter() - start
print(f'Finished in {end:.2f} s')
