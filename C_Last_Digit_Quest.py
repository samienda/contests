t = int(input())
from collections import Counter


for _ in range(t):
    n = int(input())
    
    
    a = list(map(int, input().split()))
    b = []
    count = Counter()
    for i in range(n):
        x = int(str(a[i])[-1])
        if count[x] < 3:
            b.append(x)
            count[x] += 1
            
    found = False
    for i in range(len(b) - 2):
        if found:
            break
        for j in range(i + 1, len(b) - 1):
            if found:
                break
            for k in range(j + 1, len(b)):
                if b[i] + b[j] + b[k] in [3, 13, 23]:
                    print("YES")
                    found = True
                    break
    if not found:
        print("NO")            
    
        
    