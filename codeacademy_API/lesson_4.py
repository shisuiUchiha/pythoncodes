from urllib2 import urlopen

kittens = urlopen('http://placekitten.com/g/200/300')

f = open('kittens.jpg', 'wb')
f.write(kittens.read())
f.close()
