from selenium import webdriver
from selenium.webdriver.common.by import By

#Day-12 𝐂𝐫𝐞𝐚𝐭𝐞 𝐚𝐧 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐒𝐞𝐥𝐞𝐧𝐢𝐮𝐦 𝐭𝐞𝐬𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐭𝐡𝐚𝐭 𝐯𝐞𝐫𝐢𝐟𝐲 𝐥𝐢𝐧𝐤 𝐜𝐨𝐮𝐧𝐭 𝐜𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝
# 𝐢𝐝𝐞𝐧𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐨𝐟 𝐩𝐚𝐠𝐞 𝐰𝐢𝐭𝐡 𝐦𝐚𝐱𝐢𝐦𝐮𝐦 𝐥𝐢𝐧𝐤𝐬 𝐛𝐲 𝐮𝐬𝐢𝐧𝐠 Dictionary 𝐜𝐨𝐧𝐜𝐞𝐩𝐭 𝐨𝐟 Python.

urls = {"https://www.lambdatest.com/blog/selenium-best-practices-for-web-testing/","https://www.ministryoftesting.com/articles/websites-to-practice-testing",
"https://naveenautomationlabs.com/opencart/","https://demo.guru99.com/"}
driver = webdriver.Chrome()
urlscount = dict()
for url in urls:
    driver.get(url)
    print(driver.current_url)
    print(driver.title)
    allLinks = driver.find_elements(By.TAG_NAME,"a")
    print(len(allLinks))
    urlscount[driver.title] = len(allLinks)

maxlinkInUrl = 0
pageWithMaxLink = ""
for i,j in urlscount.items():
    if j > maxlinkInUrl:
        maxlinkInUrl = j
        pageWithMaxLink = i

print("𝐏𝐚𝐠𝐞 𝐰𝐢𝐭𝐡 𝐌𝐚𝐱𝐢𝐦𝐮𝐦 𝐋𝐢𝐧𝐤𝐬: ",pageWithMaxLink," - ",maxlinkInUrl, "𝐥𝐢𝐧𝐤𝐬")