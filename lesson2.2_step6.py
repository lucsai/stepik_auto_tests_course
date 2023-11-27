from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log
import time

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID,'answer').send_keys(calc(x))
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()
    time.sleep(1)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    time.sleep(10)
    browser.quit()
