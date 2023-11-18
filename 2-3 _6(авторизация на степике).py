from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    alert.accept()
    
  #Авторизация на Степике
    # browser.get('https://stepik.org/catalog?auth=login&language=ru')
    # time.sleep(4)

    # browser.find_element(By.ID,'id_login_email').send_keys('XXXX')
    # browser.find_element(By.ID,'id_login_password').send_keys('XXXXXXX')

    # browser.find_element(By.CLASS_NAME,'sign-form__btn').click()
    # time.sleep(4)
    # browser.get('https://stepik.org/lesson/184253/step/6?unit=158843')
    # time.sleep(14)

    # answer_input = browser.find_element(By.TAG_NAME,'textarea')

    # answer_input.send_keys(answer)
    # browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    # button = browser.find_element(By.CLASS_NAME,'submit-submission')
    # time.sleep(3)
    # button.click()
    

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()
