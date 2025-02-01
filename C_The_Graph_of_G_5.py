t = int(input())

memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 2,
    8: 3,
    9: 3,
}

for _ in range(t):

    a, b = list(map(int, input().split()))
    
    if memo[a] == memo[b]:
        print('Yes')
    else:
        print('No')
