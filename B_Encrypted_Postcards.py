t = int(input())

for _ in range(t):
    
    n = int(input())
    
    s = input()
    
    a = ""
    
    left = 0
    right = 1   
    
    while right < n:
        a += s[left]
        
        while right < n and  s[left] != s[right]:
            right += 1
            
        right += 1
        left = right
        
        right += 1
        
    print(a)
        
            
    