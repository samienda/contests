n, x, y = map(int, input().split())
x, y = min(x,y), max(x, y)

def isvalid(time):
    time -= x
    
    total =  time// x + time // y
    total += 1
    return total >= n


low = 0
high = n * max(x, y)

while low < high:
    mid = (low + high) // 2
    
    if isvalid(mid):
        high = mid
    else:
        low = mid + 1
        
print(low)