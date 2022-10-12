from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox()

browser.get("https://stepik.org/lesson/25969/step/8")