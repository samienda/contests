l, r = map(int, input().split())
left, right = len(str(l)), len(str(r))
from collections import Counter
# print(left, right)
while l <= r:
    value = len(Counter(str(l)))
    # print(value) 
    if left <= value <= right:
        print(l)
        break
    
    l += 1
else:
    print(-1)