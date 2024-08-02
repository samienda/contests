n, m = map(int, input().split())
from collections import Counter


last =  -1
for i in range(n):
    
    x = input()
    count = Counter(x)
    if len(count) > 1 or last in count:
        print('NO')
        break 
    
    last = x[0]
    
else:
    print("YES")
    
