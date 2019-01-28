f = open("commentary.txt", "r")
d = ""

for line in f:
    d += line

f.close()
d = d.replace("\r", "").split("\n")

teams = d[0].split(" versus ")
points = []

for i in range(len(teams)):
    points.append(0)

for i in range(1, len(d)):
    line = d[i].split(" ")

    for j in range(len(teams)):
        if (teams[j] == line[0]):
            points[j] += 1
            break

if (points[0] > points[1]):
    print("%s %d" % (teams[0], points[0]))
    print("%s %d" % (teams[1], points[1]))
else:
    print("%s %d" % (teams[1], points[1]))
    print("%s %d" % (teams[0], points[0]))
