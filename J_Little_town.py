from collections import defaultdict, deque


n, m , s, t= map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].add(end)
    graph[end].add(start)

minn = n
queue = deque()
queue.append((s, 0))
seen = set()
seen.add(s)
from_start = [-1 for _ in range(n+1)]
from_start[s] = 0
# print(from_start)
from_end = [-1 for _ in range(n+1)]
from_end[t] = 0
while queue:
    node, dist = queue.popleft()
    if node == t:
        minn = min(minn, dist)
    for child in graph[node]:
        if child not in seen:
            seen.add(child)
            from_start[child] = dist+1
            queue.append((child, dist + 1))

queue = deque()
queue.append((t, 0))
seen = set()
seen.add(t)
while queue:
    node, dist = queue.popleft()
    for child in graph[node]:
        if child not in seen:
            seen.add(child)
            from_end[child] = dist +1
            queue.append((child, dist + 1))

count = 0
# print(from_start)
# print(from_end)
for start in range(1,1+n):
    for end in range(start+1, n+1):
        if end not in graph[start] and start not in graph[end]:
            # print("start", start, end)
            # print(from_start[start] + from_end[end] + 1, from_start[end] + from_end[start] + 1)
            if from_start[start] + from_end[end] + 1 >= minn and from_start[end] + from_end[start] + 1 >= minn:
                count += 1
print(count) 
