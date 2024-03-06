from collections import Counter


n, s = map(int, input().split())

a = list(map(int, input().split()))


count = 0

left = 0
right = 0
curr = 0
dic = Counter()

for right in range(n):
    curr += a[right]
    dic[a[right]] += 1
    
    while len(dic) > s and left < n:
        dic[a[left]] -= 1
        if dic[a[left]] == 0:
            dic.pop(a[left]) 
        left += 1
        
    count += right - left + 1
        


print(count)