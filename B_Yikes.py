n = int(input())

p = list(map(int, input().split()))

m = int(input())
que = list(map(int, input().split()))

import bisect

for i in range(1,n):
    p[i] += p[i - 1]
    
# print(p)
for q in que: 
    
    idx = bisect.bisect_left(p, q)
    
    print(idx + 1)


