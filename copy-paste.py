import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

chr_option = webdriver.ChromeOptions()
chr_option.add_argument('--incognito')
chr_option.add_argument('--start-maximized')
driver = webdriver.Chrome(options= chr_option)

driver.get("https://www.facebook.com/login/")
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("manan")
driver.find_element(By.ID,"email").send_keys(Keys.CONTROL,"a")
driver.find_element(By.ID,"email").send_keys(Keys.CONTROL,"c")
driver.find_element(By.ID,"email").send_keys(Keys.TAB)
driver.find_element(By.ID,"pass").send_keys(Keys.CONTROL,"v")
driver.find_element(By.ID,"pass").send_keys(Keys.ENTER)

driver.quit()