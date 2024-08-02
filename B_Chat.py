n, k, q = list(map(int, input().split()))
strength = list(map(int, input().split()))
import heapq


heap = []
for _ in range(q):
    typei, ids = list(map(int, input().split()))
    
    if typei == 1:
        heapq.heappush(heap, (strength[ids - 1], ids))
        if len(heap) > k:
            heapq.heappop(heap)
    else:
        if (strength[ids - 1], ids) in heap:
            print("YES")
        else:
            print("NO")
        
        
        