from selenium import webdriver
from selenium.webdriver.common.by import By
from cgitb import text
from math import sin, log
import time

# 1 Открыть страницу

link = 'http://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

# 2 Считать значение для переменной x.

x = browser.find_element(By.ID, 'input_value').text

# 3 Посчитать математическую функцию от x.

def calc(x):
    return str(log(abs(12*sin(x))))
y = calc(int(x))

# 4 Проскроллить страницу вниз.

browser.execute_script("window.scrollBy(0, 100);")

# 5 Ввести ответ в текстовое поле.

inp = browser.find_element(By.ID, 'answer')
inp.send_keys(y)

# 6.Выбрать checkbox "I'm the robot".

chekbox = browser.find_element(By.ID, 'robotCheckbox')
chekbox.click()

# 7. Переключить radiobutton "Robots rule!".

robot = browser.find_element(By.ID, 'robotsRule')
robot.click()

# 8.Нажать на кнопку "Submit".

btn_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn_submit.click()
