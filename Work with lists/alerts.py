from multiprocessing.connection import answer_challenge
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    buttonStart = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()



    def calc(elem_x):
        return str(math.log(abs(12*math.sin(int(elem_x)))))

    elem_x = browser.find_element(By.ID, "input_value").text
    y=calc(elem_x)

    answer = browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла