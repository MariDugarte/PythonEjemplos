from selenium.webdriver.common.by import By


class ProductPricePageLocators:
    PRODUCT_PRICE = (By.CLASS_NAME, 'productfilneprice')


class ProductPricePage:

    def __init__(self, driver):
        self.driver = driver

    def getProductPrice(self):
        return self.driver.find_element(*ProductPricePageLocators.PRODUCT_PRICE)
