t = int(input())


for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    zero = a.count(0)
    count = 0
    found = False
    for i in range(n): 
        if a[i] == 0:
            zero -= 1
        else:        
            count += zero
    
    
    zero = a.count(0)
    one = a.count(1)
    left, right= 0, n - 1
    scorezero = scoreone = 0
    
    while right > 0:
        if a[right] == 1:
            scoreone = one - 1 - (n - right - 1)
            break
        right -= 1
        
            
    while left < n:
        if a[left] == 0:
            scorezero = zero - left - 1 
            break
        left += 1
        
        
    count += max(scoreone, scorezero, 0)
            
    print(count) 
            