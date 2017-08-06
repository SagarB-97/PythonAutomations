from selenium import webdriver
from selenium.webdriver.common.keys import Keys


name = raw_input("Name of group/person you want to spam : ")
msg = raw_input("Type the message : ")
count = int(input("Enter count : "))

browser = webdriver.Chrome('/home/sagar/Downloads/chromedriver')
browser.get("https://web.whatsapp.com/")

xpath = "//span[@title=\'"+name+"\']"
result=0
while (result==0):
	try:
		elem = browser.find_element_by_xpath(xpath).click()
		result=1
	except:
		result=0

inputElem = browser.find_element_by_xpath("//div[@class='input']")

num = range(count+1)
for i in num:
	inputElem.send_keys(msg)
	inputElem.send_keys(Keys.ENTER)
