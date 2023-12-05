import math
import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

final = ''

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(final)

@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_authorization(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(20)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    browser.find_element(By.ID, 'id_login_email').send_keys('XXX')
    browser.find_element(By.ID, 'id_login_password').send_keys('XXX')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    browser.implicitly_wait(20)
    time.sleep(10)
    answer = str(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    check_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой
