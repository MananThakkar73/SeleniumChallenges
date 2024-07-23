import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://qaplayground.dev/apps/verify-account/")

code = driver.find_elements(By.XPATH,"//input[@class='code']")
for e in code:
    e.send_keys(Keys.NUMPAD9)

succ = driver.find_element(By.XPATH,"//*[text()='Success']").is_displayed()

assert succ == True
print("success")

driver.quit()


# keys method