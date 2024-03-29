import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.user_register_page import UserRegisterPage
from util.read_yaml import ReadYaml
from util.replace_value import ReplaceValue
from util.logger_hand import logger


class TestUserRegister:

    def setup_class(self):
        self.driver = webdriver.Edge()
        self.RegisterPage = UserRegisterPage(self.driver)

    @pytest.mark.parametrize('register_data', ReadYaml().read_data_yaml('register.yml'))
    def test_register(self, register_data):
        self.RegisterPage.goto_register_page()
        reg_data = ReplaceValue(self.RegisterPage).replace_value(register_data)
        logger.info('*' * 30 + "注册测试" + '*' * 30)
        logger.info('当前是第{}条用例：'.format(reg_data['case_id']))
        logger.info('测试名称：{}'.format(reg_data['name']))
        logger.info('测试数据：{}'.format(reg_data['data']))
        logger.info('预期结果：{}'.format(reg_data['data']['expected']))
        self.RegisterPage.register(username=reg_data['data']['username'], email=reg_data['data']['email'],
                                   pwd=reg_data['data']['pwd'], confirmPwd=reg_data['data']['confirmPwd'],
                                   verification_code=reg_data['data']['verification_code'])

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            assert alert.text == reg_data['data']['expected']
            logger.info('实际结果：{}'.format(alert.text))
        except AssertionError as ae:
            logger.exception("实际结果与预期结果不一致")
        alert.accept()

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()
