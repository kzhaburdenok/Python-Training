from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element= browser.find_element(By.ID, "input_value")
    x=x_element.text
    y=calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()
    radioButtonClick = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radioButtonClick)
    radioButtonClick.click()

    button = browser.find_element(By.TAG_NAME, "button")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла