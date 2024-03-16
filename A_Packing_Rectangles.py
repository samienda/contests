w, h, k = map(int, input().split())


low = 1
high = w * k * h

while low < high:
    
    mid = (low + high) // 2
    
    side = mid // w
    down = mid // h
    
    if side * down < k:
        low = mid + 1
    else:
        high = mid
        
print(low)