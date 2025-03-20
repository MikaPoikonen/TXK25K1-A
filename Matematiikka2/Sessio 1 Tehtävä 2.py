import numpy as np
def eka():

    a = 1.6
    b = 2.3
    ab = a*a + b*b
    c = np.sqrt(ab)
    print (c)


def toka():
    c = 6.4
    a = 2
    b = 3
    ab = a*a + b*b
    x = 6.4*6.4 / (ab)
    x = np.sqrt(x)
    print(ab)
    print (x)
    kateetti_a = x
    kateetti_b = 2*x
    print(f"Kateetti a: {kateetti_a}" + f"Kateetti b: {kateetti_b}")
toka()