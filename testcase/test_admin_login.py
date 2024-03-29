import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.logger_hand import logger
from pages.admin_login_page import AdminLoginPage
from util.read_yaml import ReadYaml
from util.replace_value import ReplaceValue
import pytest_dependency


class TestAdminLogin:
    def setup_class(self):
        self.driver = webdriver.Edge()
        self.AdminLoginPage = AdminLoginPage(self.driver)

    @pytest.mark.depandency(name='admin_login', scope='package')
    @pytest.mark.parametrize('admin_login_data', ReadYaml().read_data_yaml('admin_login.yml'))
    def test_admin_login(self, admin_login_data):
        self.AdminLoginPage.goto_admin_login_page()
        admin_log_data = ReplaceValue(self.AdminLoginPage).replace_value(admin_login_data)
        logger.info('*' * 30 + "后台登录测试" + '*' * 30)
        logger.info('当前是第{}条用例：'.format(admin_log_data['case_id']))
        logger.info('测试名称：{}'.format(admin_log_data['name']))
        logger.info('测试数据：{}'.format(admin_log_data['data']))
        logger.info('预期结果：{}'.format(admin_log_data['data']['expected']))
        self.AdminLoginPage.admin_login(
            username=admin_log_data['data']['username'],
            pwd=admin_log_data['data']['pwd'],
            verification_code=admin_log_data['data']['verification_code']
        )
        WebDriverWait(self.driver, 5).until(EC.title_is("JPress后台"))
        try:
            assert self.driver.title == admin_log_data['data']['expected']
            logger.info('实际结果：{}'.format(self.driver.title))
        except AssertionError as ae:
            logger.exception("实际结果与预期结果不一致")

    # def teardown_class(self):
    #     time.sleep(2)
    #     self.driver.quit()

