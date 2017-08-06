from lxml import html
import requests

i=1

while i<10:
	curUrl = ("http://xkcd.com/"+str(i)+"/")
	page = requests.get(curUrl)
	tree = html.fromstring(page.content)
	imgU = tree.xpath("//div[@id='comic']/img/@src")
	imageUrl = "http://"+imgU[0][2:]
	image = requests.get(imageUrl,stream=True)
	imageFile = open(str(i)+'.jpg',"wb")
	for chunk in image:
		imageFile.write(chunk)
	print("Downloaded from : "+imageUrl)
	i=i+1

print('All Done!!')
