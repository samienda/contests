n = int(input())
for i in range(n):
    s, t = input().split()
    # print(s, r)
    l, r = 0, 0
    count = 0
    while l < len(s):
        if s[l] != t[r]:
            count += 1
        l += 1
        r += 1

    print(count)
