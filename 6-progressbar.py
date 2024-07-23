import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/progressbar")

driver.find_element(By.ID,"startButton").click()

wait = WebDriverWait(driver, 30)

wait.until(EC.visibility_of_element_located((By.XPATH,"//*[starts-with(text(),'7')]")))
driver.find_element(By.ID,"stopButton").click()

res = driver.find_element(By.ID,"result").text

print(res)

driver.quit()

