n, s = map(int, input().split())


a = list(map(int, input().split()))

left = 0
curr = 0
size = n + 1
for right in range(n):
    curr += a[right]
    while curr >= s:
        size = min(size, right - left + 1)
        curr -= a[left]
        left += 1
        
    
print(size if size <= n else -1)