from collections import defaultdict
def inbound(row, col): return 0 <= row <= n and 0 <= col < 0
t = int(input())


for _ in range(t):


    for _ in range(t):
        n = int(input())

        instruction = list(input())
        graph = defaultdict(list)
        for i in range(n):

            left, right = map(int, input().split())

            if left:
                graph[i + 1].append(left)
            if right:
                graph[i + 1].append(right)

    print(graph)
