from pytest_bdd import scenarios, given, when, then, parsers
from Pages.HeaderPage import HeaderPage
from Pages.ProductPricePage import ProductPricePage


# Scenarios
scenarios('../features/SearchProductPrice.feature')


# When Steps
@when(parsers.parse('complete "{product}"'))
def complete_product(browser, product):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(product)
    print('Completed product in search input')


@when('press the search button')
def click_button(browser):
    header_page = HeaderPage(browser)
    header_page.getLupa().click()
    print('click lupa button')



# Then Steps

@then(parsers.parse('can check the product "{price}"'))
def check_product_price(browser, price):
    product_page = ProductPricePage(browser)

    assert product_page.getProductPrice().text == price
    print('check product price')