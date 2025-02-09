t = int(input())

for _ in range(t):

    n, x, m = list(map(int, input().split()))

    mini = x
    maxi = x

    for __ in range(m):
        l, r = list(map(int, input().split()))

        if l <= mini <= r:
            maxi = max(r, maxi)
            mini = min(l, mini)

        if l <= maxi <= r:
            maxi = max(r, maxi)
            mini = min(l, mini)

        # print(f'{_} index', mini, maxi)

    print(maxi - mini + 1)
