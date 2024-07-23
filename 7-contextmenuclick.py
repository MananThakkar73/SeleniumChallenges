from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qaplayground.dev/apps/context-menu/")
driver.maximize_window()

ri_cl = driver.find_element(By.ID,"msg")
shar = driver.find_element(By.XPATH,"//*[text()='Share']")
shar_list = driver.find_elements(By.CSS_SELECTOR,"ul.share-menu li span")

act = ActionChains(driver)

for sm in shar_list:
    act.context_click(ri_cl).perform()
    act.move_to_element(shar).perform()
    sm.click()
    text = driver.find_element(By.ID,"msg").text
    assert text == 'Menu item Twitter clicked' or text == 'Menu item Instagram clicked' or text == 'Menu item Dribble clicked' or text == 'Menu item Telegram clicked'


print("All social media link verified")

driver.quit()

