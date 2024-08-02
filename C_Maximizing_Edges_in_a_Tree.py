from copy import deepcopy
from collections import defaultdict, deque
n = int(input())

graph = defaultdict(list)
visted = defaultdict(bool)
for _ in range(n - 1):

    a, b = map(int, input().split())
    visted[a] = False
    visted[b] = False

    graph[a].append(b)
    graph[b].append(a)


# print(graph)
x = 0
o = 0


queue = deque([1])
ans = []
while queue:
    
    size = len(queue)
    level = []
    
    for i in range(size):
        
        node = queue.popleft()
        visted[node] = True
        
        for nbs in graph[node]:
            if not visted[nbs]:
                queue.append(nbs)
                
        level.append(node)
    
    ans.append(level)
    

wasx = False
for level in ans:
    if wasx:
        o += len(level)
        wasx = False
    else:
        x += len(level)
        wasx = True

# print(x, o)

# print(ans)

print((x * o) - (n - 1))            