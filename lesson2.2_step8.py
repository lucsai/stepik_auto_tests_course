from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    browser.find_element(By.NAME,'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('Ivanov@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, '[type=file]').send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split()[-1])
    alert.accept()

finally:
    time.sleep(1)
    browser.quit()
