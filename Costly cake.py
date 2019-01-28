# Enter your code for "Costly cake!" here.
c1sl = input("Cake 1 side length (cm): ")
c1c = input("Cake 1 cost ($): ")

c2sl = input("Cake 2 side length (cm): ")
c2c = input("Cake 2 cost ($): ")

c1sa = float(c1sl) ** 2
c2sa = float(c2sl) ** 2

c1cp = float(c1c) / c1sa
c2cp = float(c2c) / c2sa

print ("Cake 1 costs $%.2f per cm2 for %d cm2" % (c1cp, c1sa))
print ("Cake 2 costs $%.2f per cm2 for %d cm2" % (c2cp, c2sa))

if (c1cp == c2cp):
    print("Get either!")
else:
    if (c1cp < c2cp):
        print("Get cake 1!")
    else:
        print("Get cake 2!")
