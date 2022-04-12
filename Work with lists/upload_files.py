from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    firstName = browser.find_element(By.NAME, "firstname").send_keys("First Name")
    lastName = browser.find_element(By.NAME, "lastname").send_keys("Last Name")
    email = browser.find_element(By.NAME, "email").send_keys("email@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    fileUpload = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    fileUpload.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла