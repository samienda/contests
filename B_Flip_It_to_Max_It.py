t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    started = False
    count = 0
    _sum = 0
    for i in range(n):
        if a[i] > 0 and started:
            count += 1
            started = False
        elif a[i] < 0 and not started:
            started = True
            
        _sum += abs(a[i])
    
    if started:
        count += 1
        
    print(_sum, count) 
    