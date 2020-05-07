cache = {}


def expensive_seq(x, y, z):

    if x <= 0:
        return y + z
    elif cache.get((x, y, z)) != None:
        return cache[(x, y, z)]
    else:
        result = expensive_seq(x - 1, y + 1, z) + \
                expensive_seq(x - 2, y + 2, z*2) + \
                expensive_seq(x - 3, y + 3, z*3)

        cache[(x, y, z)] = result
        return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i * 2, i * 3, i * 4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    # print(expensive_seq(150, 400, 800))

# Other FIB:

# def fib(n):
#     if n <= 1:
#         return n

#     if n not in cache:
#         cache[n] = fib(n-1) + feib(n - 2)

#     return cache[n]

# for i in range(100):
#     print(fib(i))