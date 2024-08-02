n, q = map(int, input().split())

nums = list(map(int, input().split()))
queries = list(map(int, input().split()))


for query in queries:
    
    low = 0
    high = n
    while high > low:
        mid = (high + low) // 2
        
        if query > nums[mid]:
            low = mid + 1 
        else:
            high = mid
            
    print(low + 1)
    
