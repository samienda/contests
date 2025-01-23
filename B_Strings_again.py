t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))

    a = list(input())
    b = list(input())

    c = []
    a.sort()
    b.sort()
    
    # print(a, b)
    i = j = 0
    chance = k
    last = 1 if a[i] < b[j] else 0
    while i < n and j < m:
        if a[i] < b[j] and last == 1:
            c.append(a[i])
            i += 1
            last = 0
            chance = k - 1
        elif a[i] > b[j] and last == 0:
            c.append(b[j])
            j += 1
            last = 1
            chance = k - 1
        elif a[i] < b[j] and last == 0 and chance > 0:
            c.append(a[i])
            chance -= 1
            i += 1
        elif a[i] > b[j] and last == 1 and chance > 0:
            c.append(b[j])
            chance -= 1
            j += 1
        else:
            if last == 1:
                c.append(a[i])
                i += 1
                last = 0
                chance = k - 1
            else:
                c.append(b[j])
                j += 1
                last = 1
                chance = k - 1

    print("".join(c))
