
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    treasure = browser.find_element(By.ID, "treasure")
    x=treasure.get_attribute("valuex")
    y=calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()
    radioButtonClick = browser.find_element(By.ID, "robotsRule")
    radioButtonClick.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла