n , m = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))
left, right = 0, 0

res = []
while left < n and  right < m:
    if first[left] < second[right]:
       res.append(first[left])
       left += 1
    else:
       res.append(second[right])
       right += 1
       
       
while left < n:
    res.append(first[left])
    left += 1
    
while right < m:
    res.append(second[right])
    right += 1
       
       
print(*res)       

         