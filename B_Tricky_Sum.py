t = int(input())

for _ in range(t):

    n = int(input())

    minus = 0

    i = 1
    while i <= n:
        minus += i
        i *= 2

    total = (n / 2) * (1 + n)
    minus *= 2
    # print(total, minus)
    print(total - minus)
