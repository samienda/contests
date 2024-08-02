from math import ceil
t = int(input())


def isvalid(wagon):

    total = 0
    for i in range(n):
        total += (ceil(demand[i]/wagon) * time[i])

    return total <= k


for _ in range(t):

    n, k = map(int, input().split())

    demand = list(map(int, input().split()))
    time = list(map(int, input().split()))

    if sum(time) > k:
        print(-1)
        continue

    low = 1
    high = 10 ** 9

    while low < high:
        mid = (low + high) // 2

        if isvalid(mid):
            high = mid
        else:
            low = mid + 1

    print(low)
