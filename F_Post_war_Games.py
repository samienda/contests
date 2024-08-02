# t = int(input())

# for _ in range(t):

#     n, k = map(int, input().split())
#     if k == n:
#         print(0)
#         break

#     total = 0
#     left = k - 1
#     right = n - k
#     remainder = ((left)) % 2
#     remainder += ((right)) % 2

#     total += (((left) // 2) * 3)
#     total += ((right // 2) * 6)
#     total += (remainder * 1)

#     print(total)

from collections import defaultdict


n = int(input())
graph = defaultdict(list)
for _ in range(n):
    
    _from, to, weight = list(map(int, input().split()))
    graph[_from].append((to, weight))
    
print(graph)
