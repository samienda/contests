from collections import defaultdict, Counter
n, m = map(int, input().split())

graph = defaultdict(list)

for i in range(m):

    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# print(graph)
ans = [len(value) for key, value in graph.items()]
# print(ans)

count = ans.count(2)
star = Counter(ans)

if count == n and m == n:
    print("ring topology")
elif max(ans) > 2 and len(star) == 2 and ans.count(max(ans)) == 1:
    print("star topology")
elif len(star) == 2 and 1 in star and 2 in star and ans.count(1) == 2:
    print("bus topology")
else:
    print("unknown topology")
