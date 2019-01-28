def novowelsort(x):
    o = []
    for i in x:
        o.append([i, "".join(c for c in i if c not in "aeiouAEIOU")])
    
    o = sorted(o, key=lambda x: x[1])

    for i in range(len(o)):
        o[i] = o[i][0]

    return o
