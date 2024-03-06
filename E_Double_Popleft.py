n, q = map(int, input().split())

a = list(map(int, input().split()))


maxi = max(a)

from collections import deque, defaultdict
stack = deque()
dic = defaultdict(list)
last = a[0]

for i in range(1, n):
    dic[i].append([last, a[i]]) 
    if last > a[i]:
        stack.append(a[i])
    else:
        stack.append(last)
        last = a[i]
        
        
# print(dic) 
# print(stack)
   
    
    
for _ in range(q):
    query = int(input())
    
    if query < n :
        print(*dic[query][0])
    else:
        x = query % (n - 1)
        print(maxi, stack[x - 1])