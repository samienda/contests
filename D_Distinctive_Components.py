t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = set()
    
    count = 0
    res = []
    for num in a:
        left = 0
        curr = 0
        
     
        
        for right in range(n):
            if a[right] < num:
                curr += a[right]
            else:
                left = right + 1
                curr = 0
                
                
                
                
            while curr > num:
                curr -= a[left]
                left += 1
                
            if curr == num :
                count += 1
                break
            
    print(count)