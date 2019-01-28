import re

R = re.compile(r"(^|[^A-Z])[A-Z]{3}($|[^A-Z])")

total = 0
contains_tla = 0
for line in open("sentences.txt"):
  total += 1
  if R.search(line):
    contains_tla += 1

print("{0:.1f}% of sentences contain a TLA".format(contains_tla / total * 100))
