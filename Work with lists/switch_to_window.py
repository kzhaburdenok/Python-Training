from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    buttonStart = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(elem_x):
        return str(math.log(abs(12*math.sin(int(elem_x)))))

    elem_x = browser.find_element(By.ID, "input_value").text
    y=calc(elem_x)

    answer = browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print(browser.switch_to.alert.text.split(': ')[-1]) #answer code is print to terminal log

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла