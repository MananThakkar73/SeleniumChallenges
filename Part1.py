import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Milan%20Thakkar/Downloads/QE-index.html")

username = driver.find_element(By.ID,"inputEmail")
username.send_keys("manananannanan")

password = driver.find_element(By.ID,"inputPassword")
password.send_keys("mamamam")
password.send_keys(Keys.ENTER)

time.sleep(10)
#time.sleep(10)
#webinput.click()
print(driver.title)


