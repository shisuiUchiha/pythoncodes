import urllib
img = urllib.urlopen('http://s1.bia2m.biz/Movies/250%20Top%20Movies/12%20Years%20a%20Slave%20(2013)%201080p%20(Bia2Movies).mkv')
fhand = open('movie.mkv', 'w')
size = 0
while True:
	info = img.read(100000)
	if len(info) < 1 : break
	size = size + len(info)
	fhand.write(info)
print size,'characters copied.'
fhand.close()