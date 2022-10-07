from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from cgitb import text
import pytest



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
answer = math.log(int(time.time()))



@pytest.mark.parametrize('step', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, step):
    link = f"https://stepik.org/lesson/{step}/step/1"
    browser.get(link)

    enter = browser.find_element(By.CLASS_NAME, 'ember-text-area')
    enter.send_keys(str(math.log(int(time.time()))))

    browser.find_element(By.CLASS_NAME, 'submit-submission').click()

    x = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

    print(x)
    assert x ==  "Correct!"

if __name__ == '__main__':
    pytest.main()







