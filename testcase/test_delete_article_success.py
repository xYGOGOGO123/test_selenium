import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.Identify_verification_code import Identify_Verification_Code


class TestDeleteArticle:
    def __init__(self, login):
        self.login = login

    def test_delete_article_success(self):
        # 点击文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a').click()
        time.sleep(1)
        # 点击文章管理
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        time.sleep(1)

        # 找到文章链接
        Link = self.login.driver.find_element(By.XPATH,
                                              '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')

        ActionChains(self.login.driver).move_to_element(Link).perform()
        time.sleep(1)

        # 删除前文章数
        start_article_num = len(self.login.driver.find_element(By.CLASS_NAME, 'jp-actiontr'))

        # 删除文章
        del_elem = self.login.driver.find_element(By.XPATH,
                                                  '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')
        del_elem.click()

        # 删除后文章数
        end_article_num = len(self.login.driver.find_element(By.CLASS_NAME, 'jp-actiontr'))

        # 断言
        assert start_article_num == end_article_num + 1

    def test_delete_all_article_success(self):
        # 点击文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a').click()
        time.sleep(1)
        # 点击文章管理
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        time.sleep(1)

        # 选中标题
        Link = self.login.driver.find_element(By.XPATH,
                                              '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input')
        Link.click()

        # 点击批量删除
        self.login.driver.find_element(By.XPATH, '//*[@id="batchDel"]').click()

        # 处理删除弹框
        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present())
        alert = self.login.driver.switch_to.alert
        alert.accept()

        time.sleep(1)

        article_num = len(self.login.driver.find_element(By.CLASS_NAME, 'jp-actiontr'))
        assert article_num == 0
