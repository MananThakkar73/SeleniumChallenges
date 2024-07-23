
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import tkinter as tk
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/shadowdom")
driver.maximize_window()

#to access element of shadow dom
shodowele = driver.find_element(By.TAG_NAME,"guid-generator").shadow_root

shodowele.find_element(By.ID,"buttonGenerate").click()
text = shodowele.find_element(By.ID,"editField")

inputtext = driver.execute_script("return arguments[0].value;", text)

text.click()
act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("A").send_keys("C").key_up(Keys.CONTROL).perform()

#accessing clipboard
root = tk.Tk()
root.withdraw()
clip_val = root.clipboard_get()

if inputtext == clip_val:
    print("test passed")
else:
    print("test failed")