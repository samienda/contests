from math import gcd
t = int(input())
for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    factor = gcd(*a)

    have = 1
    for num in a:
        have *= (num // factor)

    
    low = 0
    high = max(a)
    
    while low < high:
        mid = (low + high) // 2
        
        if mid ** n < have:
            low = mid + 1
        else:
            high = mid
            
    # print(low)
    
    if low ** n == have:
        print('YES')
    else:
        print('NO')
            
            
