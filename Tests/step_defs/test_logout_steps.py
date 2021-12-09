from pytest_bdd import scenarios, given, when, then, parsers
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage
from Pages.LogoutPage import LogoutPage

# Constant
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/login'

# Scenarios
scenarios('../features/Logout.feature')


# Given Steps
@given('the Login Store webPage')
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

@then(parsers.parse('my account page is displayed'))
def check_account(browser):
    account_page = AccountPage(browser)

    assert account_page.getTitle().text == 'MY ACCOUNT'
    print('Account page is displayed')

@then('press the Logout button')
def click_logout_btn(browser):
    logout_page = LogoutPage(browser)

    logout_page.getLogoutBtn().click()
    print('click Logout button')

@then(parsers.parse('can logout me'))
def check_logout(browser):
    logout_page = LogoutPage(browser)

    assert logout_page.getLogoutTitle().text == 'ACCOUNT LOGOUT'
    print('Logout OK')