from collections import defaultdict, deque


n = int(input())

graph = defaultdict(list)

for i in range(n - 1):
    a, b , w = list(map(int, input().split()))
    
    graph[a].append((b, w))
    graph[b].append((a, w))
    
    
    
    
# print(graph)

visted = set()

queue = deque()
visted.add(0)
queue.append((0, 0))

maxi = 0
while queue:
    
    size = len(queue)
    for i in range(size):
        
        node, distance = queue.popleft()
        maxi = max(maxi, distance)
        
        for nbs, w in graph[node]:
            if nbs not in visted:
                visted.add(nbs)
                queue.append((nbs, distance + w))
                
print(maxi)
                
    
    
    