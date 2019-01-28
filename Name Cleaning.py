# Enter your code for "Name Cleaning" here.
import re

def contains_alpha(name):
  for c in name:
    if c.isalpha():
      return True
  return False

leading_nums = re.compile(r"^[0-9]*")
leading_caps = re.compile(r"^[A-Z]+([A-Z][a-z])")
all_caps = re.compile(r"(^| )[A-Z ]+($| )")
no_caps = re.compile(r"(^| )[^A-Z][^ ]*")

lines = []
for line in open("leaderboard.txt"):
  name, score = line.split(",")
  name = leading_nums.sub("", name).strip()
  name = leading_caps.sub(r"\1", name).strip()
  name = all_caps.sub("", name).strip()
  name = no_caps.sub("", name).strip()
  if not contains_alpha(name):
    name = "Invalid Name"
  lines.append((-int(score), name))

lines.sort()
for score, name in lines:
  print(name, -score, sep=",")
