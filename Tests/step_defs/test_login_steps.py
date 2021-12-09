from pytest_bdd import scenarios, given, when, then, parsers
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage

# Scenarios
scenarios('../features/Login.feature')


# When Steps
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


@then(parsers.parse('the error "{error_message}" is displayed'))
def error_login(browser, error_message):
    login_page = LoginPage(browser)

    assert error_message in login_page.getErrorMessage().text
    print ('The error is: '+error_message)