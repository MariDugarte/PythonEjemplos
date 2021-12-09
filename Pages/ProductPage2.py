from selenium.webdriver.common.by import By


class ProductPageLocators2:
    PRODUCT_TITLE = (By.CLASS_NAME, 'bgnone')

class ProductPage2:

    def __init__(self, driver):
        self.driver = driver

    def getProductTitle(self):
        return self.driver.find_element(*ProductPageLocators2.PRODUCT_TITLE)

