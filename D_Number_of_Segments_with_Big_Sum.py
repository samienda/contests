n, s = map(int, input().split())

a = list(map(int, input().split()))


count = 0

left = 0
right = 0
curr = 0

for right in range(n):
    curr += a[right]
    
    while curr >= s:
        curr -= a[left] 
        count += n - right
        left += 1
        
        


print(count)