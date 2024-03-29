from selenium.webdriver.common.by import By
from basepage.basepage import BasePage
from util.Identify_verification_code import Identify_Verification_Code


class AdminLoginPage(BasePage):
    username_input = (By.NAME, 'user')
    pwd_input = (By.NAME, 'pwd')
    verification_code_input = (By.NAME, 'captcha')
    verification_code_location = (By.ID, 'captchaImg')
    admin_login_button = (By.XPATH, '//button')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_admin_login_page(self):
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(AdminLoginPage.username_input)
        self.send_text(AdminLoginPage.username_input, username)

    def input_pwd(self, pwd):
        self.clear(AdminLoginPage.pwd_input)
        self.send_text(AdminLoginPage.pwd_input, pwd)

    def get_verification_code(self):
        return Identify_Verification_Code(self.driver, AdminLoginPage.verification_code_location)

    def input_verification_code(self, verification_code):
        self.clear(AdminLoginPage.verification_code_input)
        self.send_text(AdminLoginPage.verification_code_input, verification_code)

    def click_admin_login_button(self):
        self.click(AdminLoginPage.admin_login_button)

    def admin_login(self, username, pwd, verification_code):
        self.input_username(username)
        self.input_pwd(pwd)
        self.input_verification_code(verification_code)
        self.click_admin_login_button()
