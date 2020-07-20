import timeit
import time

import math
def manipulate_generator(generator, n):
    nextNumber = n+1
    while 1:
        if(not is_primo(nextNumber)):
            generator.send(nextNumber-1)
            return 0
        nextNumber = nextNumber+1



def is_primo(n):
    mult=0
    for count in range(2, n + 1):
        if (n % count == 0):
            mult += 1
        if (mult==2):
            break
    if mult>=2 and n !=2:
        return False
    return True


def is_primo_hard(n):
    raiz = int(math.sqrt(n))
    for d in range(2,raiz+1):
        if n%d == 0:
            return False
    return True
def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
start = timeit.default_timer()
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)



stop = timeit.default_timer()

print('Execução: ',float(stop-start))









