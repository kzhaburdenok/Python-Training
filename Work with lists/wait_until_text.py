from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.maximize_window()
# говорим WebDriver ждать все элементы в течение 5 секунд
#browser.implicitly_wait(5)
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element= browser.find_element(By.ID, "input_value")
    x=x_element.text
    y=calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submitButton = browser.find_element(By.ID, "solve").click()
    
    print(browser.switch_to.alert.text.split(': ')[-1]) #answer code is print to terminal log
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла