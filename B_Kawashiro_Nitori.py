t = int(input())

def check(s,n, k):
    
    left = 0
    right = n - 1
    
    while left < k:
        
        if s[left] != s[right]:return False
        
        left  += 1
        right -= 1
        
    if left > right:
        return False
    return True
    
    

for _ in range(t):
    
    n, k = list(map(int, input().split()))
    s = input()
    
    valid = check(s, n, k)
    
    if valid:
        print("YES")
    else:
        print("NO")
    
    
    