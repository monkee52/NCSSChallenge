# Enter your code for "Steganography" here.
import math

f = open("ncss-modified.bmp", "rb")
d = bytes(b" " + f.read())
f.close()

def get_WORD(d, o):
  return ((d[o + 0] & 0xFF) | ((d[o + 1] & 0xFF) << 8)) & 0xFFFF
def get_DWORD(d, o):
  return (get_WORD(d, o + 0) | (get_WORD(d, o + 2) << 16)) & 0xFFFFFFFF

offset = get_DWORD(d, 11)

data = d[offset + 1:]
out = ""

for i in range(0, math.floor(len(data) / 8) * 8, 8):
  t = chr(0
  	| ((data[i + 0] & 1) << 0)
    | ((data[i + 1] & 1) << 1)
    | ((data[i + 2] & 1) << 2)
    | ((data[i + 3] & 1) << 3)
    | ((data[i + 4] & 1) << 4)
    | ((data[i + 5] & 1) << 5)
    | ((data[i + 6] & 1) << 6)
    | ((data[i + 7] & 1) << 7))
  
  if t == "\x00":
  	break
  
  out += t

print(out)
