n =  int(input())

x = list(map(int, input().split()))
m =  int(input())
x.sort()

import bisect
for _ in range(m):
    
    q = int(input())
    
    print(bisect.bisect_right(x, q))