from okay_tests import OkaySK


# ## OKAY.SK MENU DESKTOP

# test = OkaySK(name="okaysk_menu", delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_random_menu_items(3)
# test.open_random_footer_items(3)
# test.abort()


# ## OKAY.SK MENU MOBILE

# test = OkaySK(name="okaysk_menu_mobile", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_random_menu_items(3)
# test.open_random_footer_items(3)
# test.abort()


# ## OKAY.SK FILTERS DESKTOP

# test = OkaySK(name="okaysk_filters", delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_specific_menu_item(text="Televízory")
# test.set_filter(name="výrobcovia", value="lg")
# test.set_filter(name="uhlopriečka", value="127")
# test.abort()


# ## OKAY.SK FILTERS MOBILE

# test = OkaySK(name="okaysk_filters_mobile", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_specific_menu_item(text="Televízory")
# test.set_filter(name="výrobcovia", value="lg")
# test.set_filter(name="uhlopriečka", value="127")
# test.abort()


# ## OKAY.SK SEARCH DESKTOP

# test = OkaySK(name="okaysk_search", delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.search_for(text="mobilny telefon")
# test.search_for(text="polstar")
# test.abort()


# ## OKAY.SK SEARCH MOBILE

# test = OkaySK(name="okaysk_search_mobile", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.search_for(text="mobilny telefon")
# test.search_for(text="polstar")
# test.abort()


# ## OKAY.SK UNFINISHED ORDER DESKTOP

# test = OkaySK(name="okaysk_unfinished_order", delay=3)
# test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
# test.open_product()
# test.add_to_cart()
# test.goto_checkout()
# test.choose_delivery(delivery="na moju adresu", proceed=True)
# test.choose_payment(payment="bankový prevod", proceed=False)
# test.abort()


# ## OKAY.SK UNFINISHED ORDER MOBILE

# test = OkaySK(name="okaysk_unfinished_order", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
# test.open_product()
# test.add_to_cart()
# test.goto_checkout()
# test.choose_delivery(delivery="na moju adresu", proceed=True)
# test.choose_payment(payment="bankový prevod", proceed=False)
# test.abort()


# ## OKAY.SK FINISHED COD ORDER

# test = OkaySK(name="okaysk_finished_cod_order", delay=3)
# test.open_url(url="https://www.okay.sk/collections/alkalicke-baterie?sort=price-ascending")
# test.open_product()
# test.add_to_cart()
# test.goto_checkout()
# test.choose_delivery(delivery="na moju adresu", proceed=True)
# test.choose_payment(payment="dobierka", proceed=True)
# test.abort()


# ## OKAY.SK PAYMENT GATE

# test = OkaySK(name="okaysk_payment_gate", delay=3)
# test.open_url(url="https://www.okay.sk/products/baterie-varta-energy-aaa-4ks")
# test.add_to_cart()
# test.goto_checkout()
# test.choose_delivery(delivery="na moju adresu", proceed=True)
# test.choose_payment(payment="karta", proceed=True)
# test.handle_gopay()
# test.empty_cart()
# test.abort()


# ## OKAY.SK FURNITURE SERVICES

# CATEGORIES = [
#     {
#         "name": "SEDACKY",
#         "url": "https://www.okay.sk/collections/rohove-sedacky-rozkladacie",
#         "services": [
#             "40968686796951", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
#             "40968686829719", # Montaz sedaciho nabytku a posteli
#         ],
#     },
#     {
#         "name": "POSTELE",
#         "url": "https://www.okay.sk/collections/postele",
#         "services": [
#             "40968686796951", # Odvoz a ekologicka likvidace sedaciho nabytku a posteli
#             "40968686829719", # Montaz sedaciho nabytku a posteli
#         ],
#     },
#     {
#         "name": "KUCHYNSKE LINKY ROHOVE",
#         "url": "https://www.okay.sk/collections/rohove-5",
#         "services": [
#             "40968686862487", # Montaz kuchyne (rohova)
#             "40968686928023", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
#             "41050674692247", # Likvidace dreveneho nabytku a kuchyni
#         ],
#     },
#     {
#         "name": "KUCHYNSKE LINKY ROVNE",
#         "url": "https://www.okay.sk/collections/rovne-kuchynske",
#         "services": [
#             "40968686895255", # Montaz kuchyne (rovna)
#             "40968686928023", # Demontaz, odvoz a likvidace dreveneho nabytku a kuchyni
#             "41050674692247", # Likvidace dreveneho nabytku a kuchyni
#         ],
#     }
# ]

# test = OkaySK(name="okaysk_furniture_services", delay=3)
# for category in CATEGORIES:
#     test.open_url(url=category["url"])
#     test.open_product()
#     test.add_to_cart()
#     test.check_services(services=category["services"])
#     test.empty_cart()
# test.abort()