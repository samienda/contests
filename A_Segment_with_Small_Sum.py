n, s = map(int, input().split())
a = list(map(int, input().split()))
left = 0
curr = 0
count = 0
right = 0

while right < n:
    curr += a[right]
    
    while curr > s:
        curr -= a[left]
        left += 1

    count = max(count, right - left + 1)
    right += 1
        
print(count)
    