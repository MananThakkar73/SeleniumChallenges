import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://testpages.eviltester.com/styled/challenges/growing-clickable.html")

time.sleep(10)
driver.find_element(By.ID,"growbutton").click()

print(driver.find_element(By.ID,"growbuttonstatus").text)

driver.quit()
