import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    decks = list(map(int, input().split()))
    
    heap = []
    
    total = 0
    for deck in decks:
        if deck == 0:
            if heap:
                total += - (heapq.heappop(heap))
        else:
            heapq.heappush(heap, - (deck))
            
    
    
    print(total)
    