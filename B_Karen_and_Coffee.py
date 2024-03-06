from collections import defaultdict
n, k, q = map(int, input().split())

prefix = [0] * 200002

mini = float('inf')
maxi = 0
for _ in range(n):
    l, r = map(int, input().split())
    
    prefix[l] += 1
    prefix[r + 1] -= 1
    
running = 0 
for i in range(1, 200002):    
    running += prefix[i]
    
    if running >= k:
        prefix[i] = 1
    else:
        prefix[i] = 0
        
    prefix[i] += prefix[i - 1]
    
for _ in range(q):
    a, b = map(int, input().split())
    count = prefix[b] - prefix[a - 1]
    
    print(count)
            
            
    
     