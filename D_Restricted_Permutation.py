from collections import defaultdict
import heapq


n, m = list(map(int, input().split()))

incoming = [0 for i in range(n + 1)]
graph = defaultdict(list)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    incoming[b] += 1
    
    
heap =  []    
for i in range(1, n + 1):
    if incoming[i] == 0:
        heapq.heappush(heap, i)
        

order = []
while heap:
    node = heapq.heappop(heap)
    
    for nbs in graph[node]:
        
        incoming[nbs] -= 1
        
        if incoming[nbs] == 0:
            heapq.heappush(heap, nbs)
            
    order.append(node)
    
print(*order if len(order) == n else [-1])
    

round()