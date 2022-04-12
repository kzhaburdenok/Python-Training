from lib2to3.pgen2 import driver
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.youtube.com/')
searchbox = driver.find_element(By.XPATH, '//input[@id="search"]')
searchbox.send_keys('natalia qa')

searchButton = driver.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
searchButton.click()
time.sleep(5)
driver.close()
