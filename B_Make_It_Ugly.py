from collections import deque, Counter


t = int(input())
for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    
    elem = Counter(a)
    if len(elem) == 1:
        print(-1)
        continue
    
    
    maxi = a[0]
    queue = deque(a)
    count = 0
    for i in range(n - 2):
        
        if a[i] != a[-1]:
            break
        count += 1
    
    left = 0
    while left < n - 1:
        
        if a[left] != maxi:
            right = left + 1
            
            while right < n and a[right] == maxi: 
                right += 1
                
            count = min(count, right - left - 1)
           
        left += 1 
        
        
    print(count)