from collections import Counter, defaultdict


n = int(input())

edge = []
indegree = Counter()
releated = Counter()


for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    edge.append([u, v, _])
    
    releated[v] += releated[u] + 1
    indegree[u] += 1


# print(edge)
# print(indegree)
# print('releated', releated)

def compare(i):
    return releated[i[1]]


edge.sort(key=compare, reverse=True)
# print(edge)

answer = [0 for _ in range(n - 1)]

num = 1
for u, v, _ in edge:
    if num < n - 1:
        answer[_] = num
    else:
        answer[_] = 0
        
    num += 1
        
        
for ans in answer:
    print(ans)

