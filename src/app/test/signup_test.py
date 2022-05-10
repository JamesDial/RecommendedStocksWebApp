'''
Unit testing for signup.py - 100% coverage achieved
Author: Michael McKinnon
Run command in terminal to generate coverage report:
    pytest src/app/test/signup_test.py --cov --cov-branch --cov-report html
'''


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class signupTests(unittest.TestCase):
    def setUp(self):
        self.driver = driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://u-fi.herokuapp.com")
        search = self.driver.find_element_by_id("rest")
        search.click()
        time.sleep(2)

    def test_exists(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)
        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mike@example.com")
        search = self.driver.find_element_by_name("password")
        search.send_keys("word5678")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Account already exists !"

        time.sleep(2)

        self.driver.close()

    def test_complete(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)
        search = self.driver.find_element_by_name("fname")
        search.send_keys()
        search = self.driver.find_element_by_name("lname")
        search.send_keys()
        search = self.driver.find_element_by_name("email")
        search.send_keys()
        search = self.driver.find_element_by_name("password")
        search.send_keys()

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Please fill out the form !"

        time.sleep(2)

        self.driver.close()

    def test_invalid_fname(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike1")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Password12@!")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "First name must contain only characters!"

        time.sleep(2)

        self.driver.close()

    def test_invalid_lname(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon1")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Password12@!")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Last name must contain only characters!"

        time.sleep(2)

        self.driver.close()

    def test_invalid_email(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Password12@!")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Invalid email address !"

        time.sleep(2)

        self.driver.close()

    def test_invalid_password_len_short(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Pass12@")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Not valid password!"

        time.sleep(2)

        self.driver.close()

    def test_invalid_password_len_long(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Passwords1232!@")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Not valid password!"

        time.sleep(2)

        self.driver.close()

    def test_invalid_password_no_upper_case(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("password12@")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Not valid password!"

        time.sleep(2)

        self.driver.close()

    def test_invalid_password_no_lower_case(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("PASSWORD12@")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Not valid password!"

        time.sleep(2)

        self.driver.close()

    def test_invalid_password_no_numbers(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Password!#@")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Not valid password!"

        time.sleep(2)

        self.driver.close()


    def test_invalid_password_no_special(self):
        self.driver.get("https://u-fi.herokuapp.com/register")
        print(self.driver.title)

        search = self.driver.find_element_by_name("fname")
        search.send_keys("Mike")
        search = self.driver.find_element_by_name("lname")
        search.send_keys("Mckinnon")
        search = self.driver.find_element_by_name("email")
        search.send_keys("mam96@uncw.edu")
        search = self.driver.find_element_by_name("password")
        search.send_keys("Password1123")

        search = self.driver.find_element_by_id("signup")
        search.click()

        message = self.driver.find_element_by_xpath("/html/body/div/div/h2/form/div").text
        assert message == "Not valid password!"

        time.sleep(2)

        self.driver.close()

