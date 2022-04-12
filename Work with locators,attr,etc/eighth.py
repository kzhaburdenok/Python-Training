from re import sub
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    submitBtn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btnState = submitBtn.get_attribute("disabled")
    assert btnState is None, "Btn is disabled"

    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox_checked=checkBox.get_attribute("checked")
    assert checkBox_checked is None, "Somehow it happens that checkbox is checked"

    radioPeople = browser.find_element(By.ID, "peopleRule")
    people_checked = radioPeople.get_attribute("checked")
    assert people_checked == "true", "Somehow People are not checked by default"

    radioRobot = browser.find_element(By.ID, "robotsRule")
    robot_checked = radioRobot.get_attribute("checked")
    assert robot_checked is None, "Why is it checked?"

    radioRobot.click()
    robot_checked = radioRobot.get_attribute("checked")
    assert robot_checked, "Why it's not checked?"

    time.sleep(10)
    btnState = submitBtn.get_attribute("disabled")
    assert btnState == "true", "Btn is still enabled"



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
