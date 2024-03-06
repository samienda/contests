t = int(input())


for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    a.sort()
    
    running = 1
    
    if a[0] != 1:
        print('NO')
        continue
    
    
    for i in range(1, n):
        if a[i] > running:
            print('NO')
            break
        
        running += a[i]
    else:
        print('YES')
        