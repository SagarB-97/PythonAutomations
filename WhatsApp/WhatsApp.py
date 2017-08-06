from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/home/sagar/Downloads/chromedriver')
browser.get("https://web.whatsapp.com/")


result=0
while (result==0):
	try:
		elem = browser.find_element_by_xpath("//span[@title='Doubtsweeper']").click()
		result=1
	except:
		result=0

inputElem = browser.find_element_by_xpath("//div[@class='input']")

ctr = 1
num = range(1,101)
for i in num:
	inputElem.send_keys(str(ctr))
	ctr=ctr+1
	inputElem.send_keys(Keys.ENTER)
