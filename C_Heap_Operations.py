import heapq
from collections import Counter


m = int(input())
order = []


count = Counter()
heap = []
for _ in range(m):
    command = input()
    
    if command[0] == 'i':
        _, num = command.split()
        heapq.heappush(heap, int(num))
        count[int(num)] += 1
        
    if command[0] == 'r':
        if not heap:
            order.append('insert 0')
        else:
            count[heap[0]] -= 1
            heapq.heappop(heap)
            
        
    if command[0] == 'g':
        _, num = command.split()
        
        if not count[int(num)]:
            heapq.heappush(heap, int(num))
            order.append(f'insert {num}')
            count[int(num)] += 1
            
        while heap[0] != int(num):
            order.append('removeMin')
            count[heap[0]] -= 1
            heapq.heappop(heap)
            
            
            
        
        
    order.append(command)
    
print(len(order))
for ch in order:
    print(ch)
    
    