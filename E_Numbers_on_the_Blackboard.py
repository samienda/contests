from math import gcd
t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # print(a)
    if n == 1:
        print(0)
        continue

    count = 0
    mini = min(a)
    maxi = max(a)
    if maxi == mini:
        print(0)
        continue

    if mini <= k <= maxi:
        print(-1)
        continue

    for i in range(n):
        a[i] -= k
        a[i] = abs(a[i])

    factor = gcd(*a)
    # print(a)
    for i in range(n):

        count += (a[i] // factor)

    print(count - n)
