import time
import random
import string

from selenium.webdriver import Keys
from wonderwords import RandomWord

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://qaplayground.dev/apps/tags-input-box/")
r = RandomWord()
text_box = driver.find_element(By.XPATH, "//input[@type='text']")
#methods
def countofTags():
    bef_tags = driver.find_elements(By.XPATH,"//div[@class='content']/ul/li")
    bef_tags_count = len(bef_tags)
    return bef_tags_count

def remTags():
    rem_tags = driver.find_element(By.XPATH,"//button[text()='Remove All']")
    rem_tags.click()

def addRandomTags(l):
    for n in range(l):
        text_box.send_keys(r.word(word_max_length=5, word_min_length=3))
        text_box.send_keys(Keys.ENTER)

def addSpecificTags(word):
    text_box.send_keys(word)
    text_box.send_keys(Keys.ENTER)

#𝐏𝐫𝐢𝐧𝐭 𝐭𝐡𝐞 𝐜𝐨𝐮𝐧𝐭 𝐧𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐚𝐠𝐬 & 𝐑𝐞𝐦𝐨𝐯𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐚𝐠𝐬 𝐢𝐧𝐬𝐢𝐝𝐞 𝐭𝐡𝐞 𝐛𝐨𝐱.

c1 = countofTags()
print("Before",c1)
remTags()

#𝐀𝐝𝐝 10 𝐭𝐚𝐠𝐬 𝐨𝐟 𝐚𝐧𝐲 𝐤𝐞𝐲𝐰𝐨𝐫𝐝𝐬 𝐲𝐨𝐮 𝐥𝐢𝐤𝐞.    
addRandomTags(10)

#𝐕𝐞𝐫𝐢𝐟𝐲 𝐭𝐡𝐚𝐭 𝐂𝐨𝐮𝐧𝐭 𝐨𝐟 𝐧𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐭𝐚𝐠𝐬 𝐢𝐬 "10" 𝐚𝐧𝐝 𝐩𝐫𝐢𝐧𝐭 𝐢𝐧 𝐜𝐨𝐧𝐬𝐨𝐥𝐞.
c2 = countofTags()
assert c2 == 10
print("Assertion successfull")
print("After adding 10 tags",c2)

#𝐍𝐨𝐰 𝐑𝐞𝐦𝐨𝐯𝐞 𝐚𝐥𝐥 𝐭𝐚𝐠𝐬 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐭𝐨 𝐢𝐧𝐩𝐮𝐭 "<𝐬𝐜𝐫𝐢𝐩𝐭>𝐚𝐥𝐞𝐫𝐭()</𝐬𝐜𝐫𝐢𝐩𝐭>" 𝐚𝐬 𝐤𝐞𝐲𝐰𝐨𝐫𝐝 𝐚𝐧𝐝 𝐚𝐝𝐝 𝐢𝐭.
remTags()
addSpecificTags("<𝐬𝐜𝐫𝐢𝐩𝐭>𝐚𝐥𝐞𝐫𝐭()</𝐬𝐜𝐫𝐢𝐩𝐭>")

#𝐓𝐫𝐲 𝐭𝐨 𝐠𝐞𝐭 𝐭𝐡𝐚𝐭 𝐯𝐚𝐥𝐮𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐚𝐠 𝐚𝐧𝐝 𝐩𝐫𝐢𝐧𝐭 𝐢𝐭 𝐨𝐧 𝐜𝐨𝐧𝐬𝐨𝐥𝐞. 𝐀𝐫𝐞 𝐲𝐨𝐮 𝐚𝐛𝐥𝐞 𝐭𝐨 𝐟𝐞𝐭𝐜𝐡 𝐭𝐡𝐞 𝐯𝐚𝐥𝐮𝐞 𝐨𝐫 𝐧𝐨𝐭? 𝐈𝐟 𝐲𝐞𝐬 𝐭𝐡𝐞𝐧 𝐰𝐡𝐚𝐭 𝐢𝐬 𝐩𝐫𝐢𝐧𝐭𝐞𝐝 𝐨𝐧 𝐜𝐨𝐧𝐬𝐨𝐥𝐞?
tag_name = driver.find_element(By.XPATH,"//div[@class='content']/ul/li").text
print(tag_name)

driver.quit()
