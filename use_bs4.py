import urllib
from bs4 import *

count=0
def get_url_links(url,count):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html,"html.parser")
	tags = soup('a')
	#print tags
	for tag in tags:
		string=tag.get('href',None)
		x=len(string)
		if (x<5):
			print string
			continue
		if not(string[x-4]=="." or string[x-3]=="." or string[x-5]==".") and string[0]!="?" and string[0]!=".":
			rurl=url+string
			print rurl
			count=count+1
			print count
			get_url_links(rurl,count)
		elif string[0]!="?" and string[0]!=".":
			z=url+string+"\n"
			fopen.write(z)



url = raw_input('Enter-')
fopen=open('download_links.txt','w')
get_url_links(url,count)
