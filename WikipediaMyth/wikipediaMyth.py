from lxml import html
import requests

curUrl = raw_input('Enter Wikipedia URL : ')
heading = ""
count = 1
while (heading!="Philosophy"):
	page = requests.get(curUrl)
	tree = html.fromstring(page.content)
	aTags = tree.xpath("//div[@id='mw-content-text']/p/a[1]/@href")
	firstLink = "https://en.wikipedia.org"+aTags[0]
	
	page = requests.get(firstLink)
	tree=html.fromstring(page.content)
	headingA = tree.xpath("//h1[@id='firstHeading']/text()")
	heading = headingA[0]
	print(str(count)+" . "+heading)
	count=count+1
	curUrl = firstLink
