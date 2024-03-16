n, k = map(int, input().split())


a = list(map(int, input().split()))



def calc(maximum):
    
    
    seg = 1
    curr = 0
    
    for num in a:
        if num > maximum:
            seg = k + 1
            break
        
        if curr + num > maximum:
            curr = num
            seg += 1
        else:
            curr += num
            
    return k >= seg


low = 1
high = sum(a)

while low < high:
    mid = (low + high) // 2
    
    if calc(mid):
        high = mid
    else:
        low = mid + 1
        
print(low)