from collections import defaultdict, deque


n = int(input())

array = list(map(int, input().split()))
color = list(map(int, input().split()))

graph = defaultdict(list)


for i in range(n - 1):
    graph[i + 2].append(array[i])
    graph[array[i]].append(i + 2)
    
    
# print(graph)

queue = deque()
visted = set()
visted.add(1)
lastcolor = color[0]

queue.append((1, lastcolor))
oper = 1

while queue:
    # print(queue)
    size = len(queue)
    for i in range(size):
        
        node, lastcolor = queue.popleft()
        
        for nbs in graph[node]:
            if nbs not in visted:
                if lastcolor != color[nbs - 1]:
                    oper += 1
                visted.add(nbs)
                queue.append((nbs, color[nbs - 1]))
                
print(oper)
