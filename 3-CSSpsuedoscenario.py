import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://play1.automationcamp.ir/advanced.html")

script = "return window.getComputedStyle(document.querySelector('.star-rating'),':after').getPropertyValue('content')"
star_text = driver.execute_script(script).strip("\"")
print(star_text)


driver.find_element(By.ID,"txt_rating").send_keys(star_text)
driver.find_element(By.ID,"check_rating").click()

val = driver.find_element(By.ID,"validate_rating").text
try:
    assert val == "Well done!"
    print("test pass")
except Exception as e:
    print(e)
    print("test fail")

driver.quit()


#psuedo element need to capture element with javascript and then execute script
#https://www.linkedin.com/feed/update/urn:li:activity:7168594464784027650?utm_source=share&utm_medium=member_desktop