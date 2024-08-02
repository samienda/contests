from collections import defaultdict

white = 'white'
grey = 'grey'
black = 'black'

n, m = list(map(int, input().split()))

graph = defaultdict(list)
color = defaultdict(str)
roots = set()

for _ in range(m):

    a, b = list(map(int, input().split()))
    color[a] = white
    color[b] = white

    graph[a].append(b)
    graph[b].append(a)

    roots.add(a)
    roots.add(b)


# print(graph)


def dfs(node):

    color[node] = grey
    for nbs in graph[node]:
        graph[nbs].remove(node)

        if color[nbs] == black:
            continue

        if color[nbs] == grey:
            return False

        if not dfs(nbs):
            return False

    color[node] = black
    return True


def colorBlack(node):
    color[node] = black
    for nb in graph[node]:
        if color[nb] != black:
            colorBlack(nb)


count = 0
print(roots)

visted = set()
for root in roots:
    # print(color)
    if color[root] == white and root not in visted:
        if not dfs(root):
            count += 1
        colorBlack(root)


print(count)
