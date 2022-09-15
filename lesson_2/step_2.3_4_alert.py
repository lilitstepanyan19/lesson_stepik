from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text
from math import log, sin

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(log(abs(12*sin(x))))

x = browser.find_element(By.ID, 'input_value').text
y = calc(int(x))

res = browser.find_element(By.ID, 'answer')
res.send_keys(y)

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.click()







