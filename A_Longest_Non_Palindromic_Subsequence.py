from collections import Counter


t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    left = -1 
    
    count = Counter(s)
    if len(count) > 1:
        print(n - 1)
    else:
        print(-1)
        
    
    