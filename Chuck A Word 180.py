lines = []

while True:
    x = input("Line: ")

    if (x == ""):
        break
    else:
        lines.append(" ".join(w[::-1] for w in x.split()))

for i in lines:
    print(i)
