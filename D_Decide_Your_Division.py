from collections import Counter


t = int(input())

memo = {}


def check(n):
    count = Counter()
    # print(f'n {n}')
    while n % 2 == 0:
        n /= 2
        count[2] += 1

    while n % 3 == 0:
        count[3] += 1
        n /= 3
        n *= 2
        
    while n % 5 == 0:
        count[5] += 1
        n /= 5
        n *= 2
        n *= 2

    while n % 2 == 0:
        n /= 2
        count[2] += 1
    # print(count)
    return n == 1, count[2] + count[3] + count[5]



for _ in range(t):
    n = int(input())

    valid, ans = check(n)
    if not valid:
        print(-1)
    else:
        print(ans)
        # ans = dp(n)
        # print(ans if ans != float('inf') else -1)
