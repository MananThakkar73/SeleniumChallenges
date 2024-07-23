from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumpractise.blogspot.com/2016/09/how-to-work-with-disable-textbox-or.html")

driver.implicitly_wait(5)


driver.execute_script("document.getElementById('pass').removeAttribute('disabled')")
passw = driver.find_element(By.ID,"pass")
passw_status = passw.is_enabled()
print(passw_status)

driver.quit()


#to enable disbaled field use javascript "document.getElementById('pass').removeAttribute('disabled')"
#https://www.linkedin.com/posts/kushalparikh11_50daysofcodechallenge-selenium-activity-7168225014629044224-3FuG?utm_source=share&utm_medium=member_desktop
