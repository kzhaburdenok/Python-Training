from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.ID, "num1").text
    y_elem = browser.find_element(By.ID, "num2").text

    x_elem = int(x_elem)
    y_elem = int(y_elem)
    sumToFind = x_elem + y_elem
#    sumToFind = str(sumToFind)
#    print("sum is", sumToFind)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value('%s' % sumToFind) 

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла