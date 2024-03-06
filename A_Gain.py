t = int(input())

for _ in range(t):
    n = int(input())
    
    s = list(map(int, input().split()))
    
    order = sorted(s, reverse=True)
    
    for i in range(n):
        k = 0
        if k < n - 1 and order[k] == s[i]:
            k += 1
             
        s[i] = s[i] - order[k] 
        
        
    print(*s)
        
        