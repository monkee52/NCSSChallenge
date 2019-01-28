# Enter your code for "Triple-Double-Letter" here.

import re

m = re.compile(r"([a-zA-Z])\1")

f = open("words.txt", "r")
d = ""

for l in f:
  d += l

f.close()

d = d.split("\n")
o = []

for i in range(0, len(d)):
  x = m.findall(d[i])
  u = list(set(x))
  
  if len(u) >= 3:
    o.append(d[i])

o = sorted(o, key=str.lower)

for i in o:
  print(i)
