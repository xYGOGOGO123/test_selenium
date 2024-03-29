import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.Identify_verification_code import Identify_Verification_Code


class TestWriteArticle:
    def __init__(self, login):
        self.login = login

# 添加文章
    def test_write_article_success(self):
        title = '我的文章主题'
        content = '我的文章内容'
        expected = '文章保存成功'

        # 点击文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a').click()
        time.sleep(1)
        # 点击写文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        time.sleep(1)

        # 找到文章标题框
        self.login.driver.find_element(By.XPATH, '//input[@id="article-title"]').send_keys(title)

        # 进入frame框架
        input_frame = self.login.driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(input_frame)
        self.login.driver.find_element(By.XPATH, '/html/body').send_keys(content)

        # 跳出进入主页面
        self.login.driver.switch_to.default_content()
        self.login.driver.find_element(By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        # 弹框
        loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text

        # 断言
        assert msg == expected


