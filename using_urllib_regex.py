import re
import urllib

url = raw_input("Enter the url-")

html=urllib.urlopen(url).read()

print html

links=re.findall('href=".*?"',html)

for link in links:
	print link
