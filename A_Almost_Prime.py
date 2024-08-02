n = int(input())


def count(num):

    d = 2
    primes = set()
    while d * d <= num:

        while num % d == 0:
            num //= d
            primes.add(d)
        # print(primes)
        d += 1

    if num > 1:
        primes.add(d)

    return len(primes) == 2


ans = 0
while n > 0:
    if count(n):
        ans += 1
    n -= 1

print(ans)
