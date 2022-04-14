import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class testUniqueSelector(unittest.TestCase):
    def test_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        firstName=browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        firstName.send_keys("First Name")

        lastName=browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        lastName.send_keys("Last Name") 

        email=browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("email@test.com")

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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text is different")
        
    def test_second_link(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        firstName=browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        firstName.send_keys("First Name")

        lastName=browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        lastName.send_keys("Last Name") 

        email=browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("email@test.com")

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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text is different")
if __name__ == "__main__":
    unittest.main()
