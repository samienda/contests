t = int(input())


for _ in range(t):
    n, k = map(int, input().split())
    
    s = input()
    
    count = n
    curr = 0
    left = 0
    
    for right in range(n):
        if s[right] == 'W':
            curr += 1
        k -= 1	
            
        if k < 0:
            if s[left] == 'W':
                curr -= 1
            
            k += 1    
            left += 1
            
        if k == 0:
            count = min(count, curr)
            
    print(count)