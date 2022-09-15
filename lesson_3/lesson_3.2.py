from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestForm():
    link = " http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.first').send_keys('Ann')
    input2 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.second').send_keys('Smit')
    input_mail = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.third').send_keys('mail')
    input3 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.first').send_keys('Ann')
    input4 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.second').send_keys('Smit')
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text
    def test_form(self, welcome_text):
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

class TestForm_1():
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.first').send_keys('Ann')
    input2 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.second').send_keys('Smit')
    input_mail = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.third').send_keys('mail')
    input3 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.first').send_keys('Ann')
    input4 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.second').send_keys('Smit')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text
    def test_form(self, welcome_text):
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)


if __name__ == "__main__":
    unittest.main()

