from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


class FirstTest(unittest.TestCase):
    def setup(self):
            self.browser = webdriver.Chrome()
    def test_1(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get('http://suninjuly.github.io/registration1.html')
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys('заполнить')
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys('заполнить')
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys('заполнить')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text

        needed_text = 'Congratulations! You have successfully registered!'

        self.assertEqual(needed_text,welcome_text)


    def test_2(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get('http://suninjuly.github.io/registration2.html')
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys('заполнить')
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys('заполнить')
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys('заполнить')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


        time.sleep(1)


        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text

        needed_text = 'Congratulations! You have successfully registered!'

        self.assertEqual(needed_text,welcome_text)



if __name__ == "__main__": unittest.main()



time.sleep(10)




