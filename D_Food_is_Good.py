t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    prefix = [0] * n
    prefix[0] = a[0]
    
    for i in range(1, n):
        prefix[i] += a[i] + prefix[i - 1]
        
    # print(prefix)
    
    maxi = prefix[n - 1]
    for i in range(n):
        num = prefix[i]
        if num <= 0 or (i != n - 1 and num - maxi >= 0):
            print('NO')
            break
    else:
        print('YES')