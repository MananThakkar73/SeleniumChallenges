import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.quit()

#for bypass authentication you need to pass username & credtentials in url at beginning(after https://)
#linkposturl https://www.linkedin.com/posts/kushalparikh11_50daysofcodechallenge-selenium-activity-7167888545586651137-RaDO?utm_source=share&utm_medium=member_desktop