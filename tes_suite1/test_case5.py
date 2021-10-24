# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestCase5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
            print('ok')
        except NoSuchElementException as e:
            return False

        return True

    def test_case5(self):
        driver = self.driver
        driver.get("http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/")
        assert self.is_element_present(By.XPATH, u"//button[@value='Добавить в корзину']"), 'No such element!!!'
        driver.find_element(By.XPATH, u"//button[@value='Добавить в корзину']")
        driver.find_element_by_xpath(u"//button[@value='Добавить в корзину']").click()

        assert self.is_element_present(By.XPATH, "//div[@id='messages']/div/div/strong"), 'No such element!!!'
        assert self.is_element_present(By.XPATH,
                                       "//div[@id='content_inner']/article/div/div[2]/p"), 'No such element!!!'

    def is_alert_present(self):
        try:
            alert_el = self.driver.switch_to_
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()
