def nopat():
    print(noppa)
    return
from random import randint

while True:
    noppa = randint(1, 6)
    nopat()
    if noppa == 6:
        break
