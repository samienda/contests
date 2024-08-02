m, n = map(int, input().split())

combined = [list(map(int, input().split())) + [_] for _ in range(n)]
from math import ceil,floor
# combined.sort()

def howlong(nums, m=m):
    t, z, y,_ = nums
    
    total = m * t
    total += (y * (ceil(m / z) - 1))
    
    return total

combined.sort(key=howlong)

def howmany(nums,time):
    
    low = 0
    high = 15000000
    while high > low :
        mid = ceil((low + high)/ 2)
        
        if time < howlong(nums, mid):
            high = mid - 1
        else:
            low = mid
        
        
    # print(low, high)
    return high

def isvalid(time):
    
    total = 0
    for num in combined:
        
        total += howmany(num, time)
        
    return total >= m

low = 0
high = 1500000

while low < high:
    mid = (low + high) // 2
    
    if isvalid(mid):
        high = mid
    else:
        low = mid + 1
        
print(low)

ans = [0] * n
for num in combined:
    if m <= 0:
        break
    x = howmany(num, low)
    if m > x:
        ans[num[-1]] = x
    else:
        ans[num[-1]] = m
        
    m -= x
  
print(*ans)