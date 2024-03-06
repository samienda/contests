t = int(input())

from collections import Counter
for _ in range(t):
    
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    counts = [ [i, a[i] + b[i]] for i in range(n)]
    
    ana = 0
    bis = 0
    
    counts.sort(key=lambda item:item[1], reverse=True)
    
    for _ in range(n):
        
        i = counts[_][0]
        
        if _ % 2 == 0:
            ana += a[i] - 1
        else:
            bis += b[i] - 1
                 
    print(ana - bis)
    