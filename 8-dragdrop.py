import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

driver.get("https://qaplayground.dev/apps/sortable-list/")
driver.maximize_window()
rich = ["Jeff Bezos","Bill Gates","Warren Buffett","Bernard Arnault","Carlos Slim Helu","Amancio Ortega","Larry Ellison","Mark Zuckerberg","Michael Bloomberg"]
cont = 1
wait = WebDriverWait(driver,10)
act =ActionChains(driver)
for name in rich:
    sou_pos = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(),'"+ name + "')]")))
    tar_pos = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='" + str(cont) + "']")))
    act.drag_and_drop(sou_pos,tar_pos).perform()
    cont  = cont + 1





'''
act =ActionChains(driver)
driver.implicitly_wait(15)
act.drag_and_drop(rich_1,num_list[0]).perform()
act.drag_and_drop(rich_2,num_list[1]).perform()
act.drag_and_drop(rich_3,num_list[2]).perform()
act.drag_and_drop(rich_4,num_list[3]).perform()
act.drag_and_drop(rich_5,num_list[4]).perform()
act.drag_and_drop(rich_6,num_list[5]).perform()
act.drag_and_drop(rich_7,num_list[6]).perform()
act.drag_and_drop(rich_8,num_list[7]).perform()
act.drag_and_drop(rich_9,num_list[8]).perform()
act.drag_and_drop(rich_10,num_list[9]).perform()

driver.find_element(By.ID,"check").click()

'''



driver.find_element(By.ID,"check").click()

