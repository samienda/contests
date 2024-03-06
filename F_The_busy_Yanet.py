t = int(input())

for _ in range(t):
    
    n = int(input())
    
    a = list(map(int, input().split()))
    b = sorted(a)
    mini = min(a)
    found = False
    for i in range(n):
        if found and a[i] < a[i - 1]:
            print(-1)
            break
        
        if not found and mini == a[i]:
            found = True
    else:
        print(a.index(mini))
            
        