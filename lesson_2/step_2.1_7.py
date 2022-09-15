from cgitb import text
import imp
from selenium import webdriver
from selenium.webdriver.common.by import By

import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

picture = browser.find_element(By.ID, 'treasure')
x_element = picture.get_attribute('valuex')
x = int(x_element)
y = calc(x)

res = browser.find_element(By.ID, 'answer')
res.send_keys(y)

robot = browser.find_element(By.ID, 'robotsRule')
robot.click()

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.click()