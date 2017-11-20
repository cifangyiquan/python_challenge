#!/bin/python

import sys,  urllib2,  bz2
from PIL import Image

page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read()
un = page.splitlines()[20][5:-1]
pw = page.splitlines()[21][5:-1]

i = Image.open("integrity.jpg")
p = i.load()

# what's the size of the image?
print i.size

# grab coordinates from source
coords = eval(page.splitlines()[11][10:-2])
# couldn't remember html map notation, but as there are an even number of ... numbers, lets guess at x,y,x,y,x,y,x,y...

# lets color all pixes coordinate positions red
for x in range(len(coords)/2):
	p[coords[x*2],coords[x*2+1]] = (255, 0, 0)
i.show()

# hmm, that was just an outline of the bee...
print bz2.decompress(un.decode('string_escape'))
print bz2.decompress(pw.decode('string_escape'))
