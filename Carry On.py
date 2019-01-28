# Enter your code for "Carry On" here.
import math

def carries(a, b):
  x = [str(a), str(b)]
  y = max(x, key=len)
  cc = 0
  
  if (y == x[0]):
    x[1] = x[1].zfill(len(x[0]))
  else:
    x[0] = x[0].zfill(len(x[1]))
  
  x = [list(x[0]), list(x[1])]
  
  c = 0
  o = ""
  
  for i in range(len(x[0]) - 1, -1, -1):
    t = int(x[0][i]) + int(x[1][i]) + c
    r = t % 10
    c = math.floor((t - r) / 10)
    
    if (c > 0):
      cc += 1
    o = str(r) + o
  
  return cc
