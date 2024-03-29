import time

from selenium.webdriver.common.by import By
from basepage.basepage import BasePage
from selenium.webdriver.support.select import Select


class CategoryPage(BasePage):
    click_article_location = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/a')
    click_category_location = (By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a')
    category_name_location = (By.XPATH, '//input[@name="category.title"]')
    parent_category_location = (By.XPATH, '//select[@name="category.pid"]')
    slug_location = (By.XPATH, '//input[@name="category.slug"]')
    submit_button_location = (By.XPATH, '//button')

    def __init__(self, login):
        BasePage.__init__(self, login.driver)

    def click_article(self):
        self.click(CategoryPage.click_article_location)

    def click_category(self):
        self.click(CategoryPage.click_category_location)

    def input_category_name(self, name):
        self.send_text(CategoryPage.category_name_location, name)

    def select_parent_category(self, parent_name):
        parent_category_ele = self.find_element(CategoryPage.parent_category_location)
        Select(parent_category_ele).select_by_visible_text(parent_name)

    def input_slug(self, slug):
        self.send_text(CategoryPage.slug_location, slug)

    def click_submit_button(self):
        self.click(CategoryPage.submit_button_location)

    def category(self, name, parent_name, slug):
        self.click_article()
        time.sleep(1)
        self.click_category()
        self.input_category_name(name)
        self.select_parent_category(parent_name)
        self.input_slug(slug)
        self.click_submit_button()
