from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestForm(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_form_1(self):
        self.browser.get(" http://suninjuly.github.io/registration1.html")

        input1 = self.browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.first').send_keys('Ann')
        input2 = self.browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.second').send_keys('Smit')
        input_mail = self.browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.third').send_keys('mail')
        input3 = self.browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.first').send_keys('Ann')
        input4 = self.browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.second').send_keys('Smit')
    
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_form_2(self):
        self.browser.get(" http://suninjuly.github.io/registration2.html")

        input1 = self.browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.first').send_keys('Ann')
        input2 = self.browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.second').send_keys('Smit')
        input_mail = self.browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.third').send_keys('mail')
        input3 = self.browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.first').send_keys('Ann')
        input4 = self.browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.second').send_keys('Smit')
    
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()

