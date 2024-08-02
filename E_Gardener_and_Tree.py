from collections import defaultdict, deque


t = int(input())
for _ in range(t):
    input()
    # print("in")
    n, k = list(map(int, input().split()))

    incoming = [0 for i in range(n + 1)]
    graph = defaultdict(list)

    for x in range(n - 1):
        a, b = list(map(int, input().split()))

        graph[a].append(b)
        graph[b].append(a)

        incoming[a] += 1
        incoming[b] += 1

    # print(incoming)
    # print(graph)

    queue = deque()
    for i in range(1, n + 1):
        if incoming[i] == 1:
            queue.append(i)

    removed = 0
    if k < n:
        for i in range(k):
            level = []
            size = len(queue)
            for j in range(size):
                node = queue.popleft()

                for nbs in graph[node]:

                    incoming[nbs] -= 1
                    if incoming[nbs] == 1:
                        queue.append(nbs)

                level.append(node)
            removed += len(level)
            # print(level)
        print(n - removed)
    else:
        # print("nothting")
        print(0)
