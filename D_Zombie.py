from collections import defaultdict, deque


n , m = list(map(int, input().split()))


graph = defaultdict(list)

incoming = [0 for _ in range(n)]
for _ in range(m):
    
    u, v = list(map(int, input().split()))
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
    
    incoming[u - 1] += 1
    incoming[v - 1] += 1
    
    
    
queue = deque()
visted = set()

for i in range(n):
    if incoming[i] == 1:
        queue.append((i, 0))
        


visted  = set()
def find(node):
    if incoming[node] == 1:
        return 0
    
    ans = 0
    visted.add(node)
    for nbs in graph[node]:
        
        ans = max(
            ans,
            find(nbs) if nbs not in visted else 0
        )
        
    return ans
         
        