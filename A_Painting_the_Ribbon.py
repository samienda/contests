import math


t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    
    
    same = math.ceil(n / m)
    
    tochange = n - same
    
    if k >= tochange :
        print("NO")
    else:
        print("YES")