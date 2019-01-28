# Enter your code for "camelCase" here.
def to_camel(ident):
    def a(x):
        return x
    
    def b(x):
        return x[0].upper() + x[1::]
    
    def c():
        yield a
        while True:
            yield b

    d = c()

    return "".join(d.__next__()(x) for x in ident.split("_"))
