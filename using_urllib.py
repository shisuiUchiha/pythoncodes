import urllib
import re
from bs4 import *

url=raw_input("enter url-")
fhand = urllib.urlopen(url).read()
print fhand
fhand.close()
