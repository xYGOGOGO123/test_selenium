from selenium.webdriver.common.by import By
from basepage.basepage import BasePage
from util.Identify_verification_code import Identify_Verification_Code


class UserRegisterPage(BasePage):
    username_input = (By.NAME, 'username')
    email_input = (By.NAME, 'email')
    pwd_input = (By.NAME, 'pwd')
    confirmPwd_input = (By.NAME, 'confirmPwd')
    verification_code_input = (By.NAME, 'captcha')
    verification_code_location = (By.ID, 'captchaimg')
    register_button = (By.XPATH, '//button')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_register_page(self):
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(UserRegisterPage.username_input)
        self.send_text(UserRegisterPage.username_input, username)

    def input_email(self, email):
        self.clear(UserRegisterPage.email_input)
        self.send_text(UserRegisterPage.email_input, email)

    def input_pwd(self, pwd):
        self.clear(UserRegisterPage.pwd_input)
        self.send_text(UserRegisterPage.pwd_input, pwd)

    def input_confirmPwd(self, confirmPwd):
        self.clear(UserRegisterPage.confirmPwd_input)
        self.send_text(UserRegisterPage.confirmPwd_input, confirmPwd)

    def get_verification_code(self):
        return Identify_Verification_Code(self.driver, UserRegisterPage.verification_code_location)

    def input_verification_code(self, verification_code):
        self.clear(UserRegisterPage.verification_code_input)
        self.send_text(UserRegisterPage.verification_code_input, verification_code)

    def click_register_button(self):
        self.click(UserRegisterPage.register_button)

    def register(self, username, email, pwd, confirmPwd, verification_code):
        self.input_username(username)
        self.input_email(email)
        self.input_pwd(pwd)
        self.input_confirmPwd(confirmPwd)
        self.input_verification_code(verification_code)
        self.click_register_button()
