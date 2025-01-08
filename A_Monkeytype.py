t = int(input())


def position(c): return alpha.index(c)


for _ in range(t):
    alpha = input()
    s = input()
    last = position(s[0])
    ans = 0
    for c in s:
        ans += abs(last - position(c))
        last = position(c)

    print(ans)
