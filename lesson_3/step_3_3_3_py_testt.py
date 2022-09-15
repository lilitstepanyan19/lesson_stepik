from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_form_1():
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/registration1.html")

    input1 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.first').send_keys('Ann')
    input2 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.second').send_keys('Smit')
    input_mail = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.third').send_keys('mail')
    input3 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.first').send_keys('Ann')
    input4 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.second').send_keys('Smit')
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.close()
       
def test_form_2():
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.first').send_keys('Ann')
    input2 = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.second').send_keys('Smit')
    input_mail = browser.find_element(By.CLASS_NAME, 'first_block>.form-group>.third').send_keys('mail')
    input3 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.first').send_keys('Ann')
    input4 = browser.find_element(By.CLASS_NAME, 'second_block>.form-group>.second').send_keys('Smit')
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.close()

if __name__ == "__main__":
    pytest.main()

