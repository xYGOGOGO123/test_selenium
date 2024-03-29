from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.user_login_page import UserLoginPage
import pytest
import time
from util.logger_hand import logger
from util.read_yaml import ReadYaml


class TestUserLogin:
    def setup_class(self):
        self.driver = webdriver.Edge()
        self.LoginPage = UserLoginPage(self.driver)

    @pytest.mark.parametrize('login_data', ReadYaml().read_data_yaml('login.yml'))
    def test_user_login(self, login_data):
        self.LoginPage.goto_login_page()
        logger.info('*' * 30 + "登录测试" + '*' * 30)
        logger.info('当前是第{}条用例：'.format(login_data['case_id']))
        logger.info('测试名称：{}'.format(login_data['name']))
        logger.info('测试数据：{}'.format(login_data['data']))
        logger.info('预期结果：{}'.format(login_data['data']['expected']))
        self.LoginPage.login(username=login_data['data']['username'], pwd=login_data['data']['pwd'])

        if login_data['name'] == "登录成功":
            WebDriverWait(self.driver, 5).until(EC.title_is("用户中心"))
            try:
                assert self.driver.title == login_data['data']['expected']
                logger.info('实际结果：{}'.format(self.driver.title))
            except AssertionError as ae:
                logger.exception("实际结果与预期结果不一致")
        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            try:
                assert alert.text == login_data['data']['expected']
                logger.info('实际结果：{}'.format(alert.text))
            except AssertionError as ae:
                logger.exception("实际结果与预期结果不一致")
            alert.accept()

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

