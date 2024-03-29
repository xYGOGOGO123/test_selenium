from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def send_text(self, loc, text):
        self.driver.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.driver.find_element(*loc).click()

    def clear(self, loc):
        self.driver.find_element(*loc).clear()

    def get_title(self):
        return self.driver.title


