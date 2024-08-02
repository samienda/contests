import math
n, r = map(int, input().split())
a = list(map(int, input().split()))
r /= 100
# print(r)

def isvalid(value):
    
    rem = 0
    for num in a:
        if num > value:
            rem += (num - value) * (1 - r)
        else:
            rem -= (value - num)
            
    return rem >= 0


low = min(a)
high = max(a)

while high - low > 0.00000001:
    mid = (low + high) / 2
    # print(mid)
    if isvalid(mid):
        low = mid
    else:
        high = mid 

print(low)