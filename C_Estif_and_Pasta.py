import sys
k = int(input())


sys.setrecursionlimit(1 << 30)

total = 6
mod = 10**9 + 7

nodes = (2 ** (k)) - 1

memo = {}


def find(n):
    x = '1' * n
    # print(x[0])
    return int(x, 2)


x = find(2 * (nodes - 1))
# print(total % mod)
# print('fine')
x %= mod
x *= 6
print((x % mod) + 6)
