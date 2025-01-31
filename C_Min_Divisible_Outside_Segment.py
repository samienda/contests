t = int(input())
import math
for _ in range(t):
    
    l, r, d = list(map(int, input().split()))
    
    
    
    left = l / d
    right = r / d
    
    
    if left > 1 :
        print(d)
    else:
        print(math.floor(right + 1) * d)
        
        