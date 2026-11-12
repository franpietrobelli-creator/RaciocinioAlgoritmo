def f(x):
    return x**2

def g(p, q):
    s = p**(0.5)-3*q
    return s

print(f(3))
print(g(9, 2))

def h(x):
    if x == 0:
        return "Erro"
    return 1/x

def i(x):
    return x+1
def j(x):
    return x**2
print(i(g(5)))
print(j(g(5)))