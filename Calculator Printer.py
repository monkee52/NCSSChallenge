# Enter your code for "Calculator Printer" here.
x = input("Number: ")
y = int(input("Width: "))

sx = y + 2
sy = 2 * y + 3

o = []

for i in x:
    if i == "0":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
            
        p.append(" " + (" " * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)
    elif i == "1":
        p = []

        p.append(" " + (" " * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
            
        p.append(" " + (" " * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
        
        p.append(" " + (" " * y) + " ")
        o.append(p)
    elif i == "2":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + " ")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)
    elif i == "3":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)
    elif i == "4":
        p = []

        p.append(" " + (" " * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
        
        p.append(" " + (" " * y) + " ")
        o.append(p)
    elif i == "5":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + " ")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)
    elif i == "6":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + " ")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)
    elif i == "7":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
            
        p.append(" " + (" " * y) + " ")
        
        for j in range(y):
            p.append(" "  + (" " * y) + "|")
        
        p.append(" " + (" " * y) + " ")
        o.append(p)
    elif i == "8":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)
    elif i == "9":
        p = []

        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append("|" + (" " * y) + "|")
            
        p.append(" " + ("-" * y) + " ")
        
        for j in range(y):
            p.append(" " + (" " * y) + "|")
        
        p.append(" " + ("-" * y) + " ")
        o.append(p)

for i in range(sy):
    x = []

    for j in range(len(o)):
        x.append(o[j][i])

    print(" ".join(x))
