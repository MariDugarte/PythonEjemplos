from selenium.webdriver.common.by import By


class LogoutPageLocators:
    USER_INPUT = (By.ID, 'loginFrm_loginname')
    PASS_INPUT = (By.ID, 'loginFrm_password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[title="Login"]')
    LOGOUT_BTN = (By.CSS_SELECTOR, '.side_account_list > li:nth-of-type(10) > a')
    LOGOUT_TITLE = (By.CLASS_NAME, 'maintext')



class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    def getUserInput(self):
            return self.driver.find_element(*LogoutPageLocators.USER_INPUT)

    def getPassInput(self):
            return self.driver.find_element(*LogoutPageLocators.PASS_INPUT)

    def getLoginBtn(self):
            return self.driver.find_element(*LogoutPageLocators.LOGIN_BTN)

    def getLogoutBtn(self):
        return self.driver.find_element(*LogoutPageLocators.LOGOUT_BTN)

    def getLogoutTitle(self):
        return self.driver.find_element(*LogoutPageLocators.LOGOUT_TITLE)

