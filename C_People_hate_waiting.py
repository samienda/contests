n = int(input())


t = list(map(int, input().split()))

t.sort()
# p = [0] * (n + 1)
# for i in range(1, n + 1):
#     p[i] += t[i - 1] + p[i - 1]
    
# # print(p)
# # print(t)

# left = 0
# right = 0
# k = 0
# while left < n and  right < n:
#     while right + 1 < n and p[left] > t[right]:
#         # print(left, right)
#         k += t[right]
#         p[left + 1] += (t[right + 1] - k)
#         right += 1
#         # print(p)
    
#     if p[left] <= t[right]: 
#         left += 1
        
#     right += 1

# print(left)
        
wait = 0
count = 0

for t1 in t:
    if t1 >= wait: 
        wait += t1
        count += 1
        
print(count)    
