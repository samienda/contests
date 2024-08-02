from collections import defaultdict, deque


n, m = list(map(int, input().split()))

graph = defaultdict(list)

incoming = [0 for i in range(n + 1)]
for i in range(n + m - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    incoming[b] += 1


# print(graph)
# print(incoming)


queue = deque()
for i in range(1, n + 1):
    if incoming[i] == 0:
        queue.append(i)
        
answer = [0 for i in range(n + 1)]
while queue:
    
    node = queue.popleft()
    # print(node)
    for nbs in graph[node]:
        
        incoming[nbs] -= 1
        if incoming[nbs] == 0:
            queue.append(nbs)
            answer[nbs] = node
            
for i in range(1, n + 1):
    print(answer[i])
    
            
