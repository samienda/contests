n, k = map(int, input().split())

ropes = [int(input()) for _ in range(n)]


def isvalid(size):
    
    num = 0
    
    for rope in ropes:
        num += (rope//size)
    
    return num >= k


low = 0.000001
high = 10**7

while high - low > 1/10**6:
    
    mid = (low + high) / 2
    if isvalid(mid):
        low = mid
    else:
        high = mid

print(low)
         