from collections import defaultdict, deque


n, m = list(map(int, input().split()))

incoming = {}
graph = defaultdict(list)
for i in range(m):

    a, b = list(input().split())

    graph[a].append(b)
    incoming[b] = 1 + incoming.get(b, 0)
    incoming[a] = 0 + incoming.get(a, 0)


queue = deque()
for i in incoming:
    if incoming[i] == 0:
        queue.append(i)

# print(queue)
answer = []
while queue:
    node = queue.popleft()
    for nbs in graph[node]:
        incoming[nbs] -= 1
        if incoming[nbs] == 0:
            queue.append(nbs)

    answer.append(node)

print(*answer if n == len(answer) else ["IMPOSSIBLE"])
