import math
import random


def build_lookup_table():
    table = {}
    for x in range(2, 14):
        for y in range(3, 6):
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            table[(x, y)] = v

    return table


slowfun_table = build_lookup_table()


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    return slowfun_table[(x, y)]


# Ranges include lower bound but NOT upper bound
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')