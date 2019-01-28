def caesar_shift(s, n):
    o = ""
    
    for i in s:
        x = ord(i)
        
        if i.isalpha():
            xn = 0

            if i.lower() == i:
                xn = (x - 97 + n) % 26 + 97
            else:
                xn = (x - 65 + n) % 26 + 65
            
            o += chr(xn)
        else:
            o += chr(x)
    return o
