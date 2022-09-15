from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
btn.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(log(abs(12*sin(x))))

x = browser.find_element(By.ID, 'input_value').text
y = calc(int(x))

res = browser.find_element(By.ID, 'answer')
res.send_keys(y)

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.click()











