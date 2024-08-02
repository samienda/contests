# from collections import defaultdict, deque

# def answer():
#     a, b = map(int, input().split())
#     graph = defaultdict(list)
#     visited = set()
#     visited.add(1)
#     for i in range(b):
#         l, r = map(int, input().split())
#         graph[l].append(r)
#         graph[r].append(l)
        
#     que = deque()
#     que.append(1)
#     while que:
#         node = que.popleft()
#         if node == a: 
#             return 'YES'
#         for child in graph[node]:
#             if child not in visited:
#                 que.append(child)
#                 visited.add(child)
#     return 'NO'
                

# m = int(input())
# for i in range(m):
#     print(answer())


def find(num):
    while num != parent[num]:
        parent[num] = parent[parent[num]]
        num = parent[num]
    return num

def union(a, b):
    # print(rank)
    parent1 = find(a)
    parent2 = find(b)


    if parent1 != parent2:
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent2] > rank[parent1]:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1
            rank[parent1] += 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    parent = {i:i for i in range(1, n+1)}
    rank = [0 for i in range(n+1)]
    for i in range(m):
        start, dest = map(int, input().split())
        union(start, dest)
    if find(1) == find(n):
        print("YES")
    else:
        print("NO")
    