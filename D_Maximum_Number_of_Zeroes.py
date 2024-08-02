from collections import defaultdict
from math import gcd

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = defaultdict(int)

total = 0
for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            total += 1
    else:

        while gcd(a[i], b[i]) != 1:
            x = gcd(a[i], b[i])
            a[i] //= x
            b[i] //= x

        y = (-1 * b[i] * (a[i] // abs(a[i])))
        z = abs(a[i])
        count[(y, z)] += 1


if count:
    total += sorted(count.items(), key=lambda item: item[1])[-1][1]

# print(count)
print(total)
