import re

R = re.compile(r'<img [^>]*src="([^"]+)"')

for line in open("site.html"):
  for match in R.findall(line):
    print(match)
