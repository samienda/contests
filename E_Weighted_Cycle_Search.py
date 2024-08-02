from collections import defaultdict, deque


def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


t = int(input())
for _ in range(t):

    graph = defaultdict(list)
    n, m = list(map(int, input().split()))
    edges = []
    parent = {}
    rank = {}

    for _ in range(m):
        u, v, w = list(map(int, input().split()))

        edges.append([u, v, w])
        graph[u].append(v)
        graph[v].append(u)

        parent[u] = u
        parent[v] = v
        
        rank[u] = 0
        rank[v] = 0

    # print(parent)
    edges.sort(key=lambda item: item[-1], reverse=True)

    # print(edges)

    maxi = None
    for u, v, w in edges:
        rootu = find(u)
        rootv = find(v)

        if rootu != rootv:
            if rank[rootu] > rank[rootv]:
                parent[rootv] = rootu
            elif rank[rootv] < rank[rootu]:
                parent[rootu] = rootv
            else:
                parent[rootv] = rootu
                rank[rootu] += 1
                
        else:
            maxi = [u, v, w]

    # print("maximum", maxi)
    src, dest, weight = maxi
    queue = deque()
    queue.append([src, [src]])
    graph[src].remove(dest)

    visted = set()

    found = False
    while queue and not found:

        node, path = queue.popleft()

        for nbs in graph[node]:
            if nbs not in visted:
                queue.append([nbs, path + [nbs]])
                visted.add(nbs)
                
                if nbs == dest:
                    found = True
                    path.append(nbs)
                    break


    print(weight, len(path))
    print(*path)
