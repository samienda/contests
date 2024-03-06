n, m = map(int, input().split())


f = list(map(int, input().split()))
s = list(map(int, input().split()))


left = 0
right = 0
res = []
while right < m:
    while left < n and f[left] < s[right]: 
        left += 1
        
    res.append(left)
    
    right += 1
    
print(*res)
