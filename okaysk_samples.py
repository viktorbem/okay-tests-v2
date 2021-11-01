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


## OKAY.SK UNFINISHED ORDER MOBILE

test = OkaySK(name="okaysk_unfinished_order", is_mobile=True, delay=3)
test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="bankový prevod", proceed=False)
test.abort()