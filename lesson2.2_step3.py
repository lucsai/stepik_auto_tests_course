from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,'num1').text
    y = browser.find_element(By.ID,'num2').text
    z = int(x) + int(y)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла