import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver


# Constant
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/login'


@pytest.fixture
def browser():
    #b = webdriver.Firefox()
    b = webdriver.Chrome('../../Drivers/chromedriver.exe')
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps
@given('the Login Store webPage')
@given('the search is in the header')
@given('the Logout Store webPage')
def open_store_web(browser):
    browser.get(STORE_WEB)
    print('Open Store webPage')


@when(parsers.parse('complete "{username}" and "{password}"'))
def complete_user_pass(browser, username, password):
    login_page = LoginPage(browser)

    login_page.getUserInput().send_keys(username)
    login_page.getPassInput().send_keys(password)
    login_page.getLoginBtn().click()
    print('User and password are completed')


# Then Steps
@then(parsers.parse('my account page is displayed'))
def check_account(browser):
    account_page = AccountPage(browser)

    assert account_page.getTitle().text == 'MY ACCOUNT'
    print('Account page is displayed')