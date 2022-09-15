from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

fname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
fname.send_keys('Ann')

lname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
lname.send_keys('Ann')

mail = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
mail.send_keys('bla')


file_path = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.dirname(__file__)  ??????????
fp = os.path.join(file_path, 'file.txt')

inp_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
inp_file.send_keys(fp)

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.click()


