import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chromeoptions = Options()
chromeoptions.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\Milan Thakkar\\PycharmProjects\\Pythonbasic\\SeleniumPractice\\downloads"})
driver = webdriver.Chrome(options=chromeoptions)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/FileDownload.html")

down_button = driver.find_element(By.XPATH,"//a[@class='btn btn-primary']")
text_area = driver.find_element(By.ID,"textbox")

act = ActionChains(driver)
act.move_to_element(text_area).perform()

down_button.click()

time.sleep(5)