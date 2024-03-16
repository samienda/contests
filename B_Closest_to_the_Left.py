n, k = map(int, input().split())

a = list(map(int, input().split()))
q = list(map(int, input().split()))

for target in q:
    
    low = 0
    high = n 
    
    while low < high:
        
        mid = (low + high) // 2
        
        if target >= a[mid]:
            low = mid + 1
        else:
            high = mid
            
    print(low)