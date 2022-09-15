from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from cgitb import text

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text

sum = int(num1) + int(num2)

select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value(str(sum))

btn = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()






