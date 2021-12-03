from okay_tests import OkayTest


# ## OKAY.SK MENU DESKTOP

# test = OkayTest(name="okaysk_menu", delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_random_menu_items(3)
# test.open_random_footer_items(3)
# test.abort()


# ## OKAY.SK MENU MOBILE

# test = OkayTest(name="okaysk_menu_mobile", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_random_menu_items(3)
# test.open_random_footer_items(3)
# test.abort()


# ## OKAY.SK FILTERS DESKTOP

# test = OkayTest(name="okaysk_filters", delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_specific_menu_item(text="Televízory")
# test.set_filter(name="výrobcovia", value="lg")
# test.set_filter(name="uhlopriečka", value="55")
# test.abort()


# ## OKAY.SK FILTERS MOBILE

# test = OkayTest(name="okaysk_filters_mobile", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.open_specific_menu_item(text="Postele")
# test.set_filter(name="rozmery", value="180 x 200")
# test.set_filter(name="úložný priestor", value="ano")
# test.abort()


# ## OKAY.SK SEARCH DESKTOP

# test = OkayTest(name="okaysk_search")
# test.open_url(url="https://www.okay.sk/")
# test.search_for(text="mobilny telefon")
# test.search_for(text="vankúš")
# test.search_for(text="predajne")
# test.search_for(text="iphone v akcii")
# test.search_for(text="nintendo")
# test.search_for(text="ako vybrať")
# test.abort()


# ## OKAY.SK SEARCH MOBILE

# test = OkayTest(name="okaysk_search_mobile", is_mobile=True, delay=3)
# test.open_url(url="https://www.okay.sk/")
# test.search_for(text="mobilny telefon")
# test.search_for(text="bratislava")
# test.search_for(text="splátky")
# test.search_for(text="doprava")
# test.abort()


# ## OKAY.SK UNFINISHED ORDER DESKTOP

# test = OkayTest(name="okaysk_unfinished_order", delay=3)
# test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
# test.open_product()
# test.add_to_cart()
# test.goto_checkout()
# test.choose_delivery(delivery="na moju adresu", proceed=True)
# test.choose_payment(payment="bankový prevod", proceed=False)
# test.abort()


## OKAY.SK UNFINISHED ORDER MOBILE

test = OkayTest(name="okaysk_unfinished_order", is_mobile=True, delay=3)
test.open_url(url="https://www.okay.sk/collections/mobilne-telefony-4")
test.open_product()
test.add_to_cart()
test.goto_checkout()
test.choose_delivery(delivery="na moju adresu", proceed=True)
test.choose_payment(payment="bankový prevod", proceed=False)
test.abort()