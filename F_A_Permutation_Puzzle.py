from math import lcm

t = int(input())
for _ in range(t):

    n = int(input())

    s = list(input())
    p = list(map(int, input().split()))

    count = n
    ans = []
    visted = set()

    wasstring = s[:]
    newstring = [1 for i in range(n)]

    oper = 0
    while count:
        oper += 1
        for i in range(n):
            newstring[i] = wasstring[p[i] - 1]

            if newstring[i] == s[i]:
                if i not in visted:
                    count -= 1
                ans.append(oper)
                visted.add(i)

        # print(wasstring)
        # print(newstring)
        wasstring = newstring[:]


    # print(ans, count)
    print(lcm(*ans))
