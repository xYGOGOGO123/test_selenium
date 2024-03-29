from selenium.webdriver.common.by import By
from basepage.basepage import BasePage


class UserLoginPage(BasePage):
    username_input = (By.NAME, 'user')
    pwd_input = (By.NAME, 'pwd')
    login_button = (By.XPATH, '//button')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_login_page(self):
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(UserLoginPage.username_input)
        self.send_text(UserLoginPage.username_input, username)

    def input_pwd(self, pwd):
        self.clear(UserLoginPage.pwd_input)
        self.send_text(UserLoginPage.pwd_input, pwd)

    def click_login_button(self):
        self.click(UserLoginPage.login_button)

    def login(self, username, pwd):
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login_button()