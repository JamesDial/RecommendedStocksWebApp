'''
Unit testing for models.py - 100% coverage achieved
Author: James Dial
Run command in terminal to generate coverage report:
    pytest app/test/login_test.py --cov --cov-branch --cov-report html
'''



import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://u-fi.herokuapp.com/login")

    def test_logout_test(self):
        ID = self.driver.session_id
        print("ID: ",ID)
        actual = "https://u-fi.herokuapp.com/login"
        expected = self.driver.current_url
        time.sleep(2)
        assert actual == expected
        self.driver.close()

    def test_valid_user_test(self):
        search = self.driver.find_element_by_name("email")
        search.send_keys("james@example.com")
        search = self.driver.find_element_by_name("password")
        search.send_keys("marv8902")

        search = self.driver.find_element_by_class_name("btn")
        search.click()

        actualURL = "https://u-fi.herokuapp.com/dashboard"
        expectedURL = self.driver.current_url

        time.sleep(2)
        assert actualURL == expectedURL
        self.driver.close()

    def test_invalid_user_test(self):
        search = self.driver.find_element_by_name("email")
        search.send_keys("jn@gmail.com")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Password1!")
        search = self.driver.find_element_by_class_name("btn")
        search.click()
        expected = "https://u-fi.herokuapp.com/login"
        actual = self.driver.current_url

        time.sleep(2)
        assert actual == expected
        self.driver.close()




