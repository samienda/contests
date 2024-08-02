from collections import defaultdict, deque


n = int(input())

array = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(1,n + 1):
    if i - array[i - 1] > 0:
        graph[i ].append(i - array[i - 1])

    if i + array[i - 1] < n + 1:
        graph[i].append(i + array[i - 1])


# print(graph)


def calc(i):
    target = array[i - 1] % 2

    queue = deque()
    visted = set()

    queue.append((i, 0))
    visted.add(i)

    while queue:

        size = len(queue)
        for _ in range(size):

            node, distance = queue.popleft()

            if target != array[node - 1] % 2:
                return distance

            for nbs in graph[node]:
                if nbs not in visted:
                    queue.append((nbs, distance + 1))
                    visted.add(nbs)

    return -1

ans = []
for i in range(1, n + 1):
    ans.append(calc(i))
    
print(*ans)
