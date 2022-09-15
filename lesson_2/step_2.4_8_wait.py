from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cgitb import text
from math import log, sin


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


wait = WebDriverWait(browser, 12)
el = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))


btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
btn.click()

def calc(x):
    return str(log(abs(12*sin(x))))

x = browser.find_element(By.ID, 'input_value').text
y = calc(int(x))

res = browser.find_element(By.ID, 'answer')
res.send_keys(y)

btn = browser.find_element(By.ID, 'solve')
btn.click()







