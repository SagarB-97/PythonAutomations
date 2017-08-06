from selenium import webdriver
from lxml import html
import requests

browser = webdriver.Chrome('/home/sagar/Downloads/chromedriver')

browser.get("https://10fastfingers.com/typing-test/english")
page = browser.page_source
tree = html.fromstring(page)

words = tree.xpath("//span[@wordnr]/text()")

elem = browser.find_element_by_xpath("//input[@id='inputfield']")
elem.click()

for word in words:
	elem.send_keys(word+" ")

print(words)
