import time
import pytest
from testcase.test_admin_login import TestAdminLogin
from util.logger_hand import logger
from util.read_yaml import ReadYaml
from pages.category_page import CategoryPage


class TestCategory:
    def setup_class(self):
        self.login = TestAdminLogin()
        self.CategoryPage = CategoryPage(self.login)

    @pytest.mark.depandency(depends=['admin_login'], scope='module')
    @pytest.mark.parametrize('category_data', ReadYaml().read_data_yaml('category.yml'))
    def test_category(self, category_data):
        logger.info('*' * 30 + "后台登录测试" + '*' * 30)
        logger.info('当前是第{}条用例：'.format(category_data['case_id']))
        logger.info('测试名称：{}'.format(category_data['name']))
        logger.info('测试数据：{}'.format(category_data['data']))
        self.CategoryPage.category(
            name=category_data['data']['category_name'],
            parent_name=category_data['data']['parent_name'],
            slug=category_data['data']['slug']
        )

    def teardown_class(self):
        time.sleep(2)
        self.login.driver.quit()