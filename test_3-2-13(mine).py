from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class Test_text(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_first = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        input_first.send_keys("some text")
        input_second = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        input_second.send_keys("some text")
        input_third = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        input_third.send_keys("some text")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be 'Congratulations! You have successfully registered!'")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_first = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        input_first.send_keys("some text")
        input_second = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        input_second.send_keys("some text")
        input_third = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        input_third.send_keys("some text")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!","Should be 'Congratulations! You have successfully registered!'")


if __name__ == "__main__": unittest.main()

