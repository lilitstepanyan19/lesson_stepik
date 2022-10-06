from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

answer = math.log(int(time.time()))

link = 'https://stepik.org/lesson/236895/step/1'

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)


enter = browser.find_element(By.CLASS_NAME, '#ember90')
enter.send_keys(answer)

submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
