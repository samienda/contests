import heapq


t = int(input())
for _ in range(t):
    n = int(input())

    array = list(map(int, input().split()))
    
    heap = []
    for i, num in enumerate(array):
        if num:
            heapq.heappush(heap, (-num, i))
    
    total = 0

    answer = []
    while heap:
        # print("heap", heap)
        first = -1
        second = -1
        if heap:
            first, i = heapq.heappop(heap)
            first = abs(first)
        if heap:
            second, j = heapq.heappop(heap)
            second = abs(second)
        # print(first, second)
        if -1 not in [first, second]:
            left = abs(first - second)
            
            if left:    
                heapq.heappush(heap, (-left, i))
            answer.append((i + 1, j + 1, abs(second)))
            total += abs(second)
                
    # print(answer)
    print(total)
    for i, j, times in answer:
        mini = min(i, j)
        maxi = max(i, j)
        
        for _ in range(times):
            print(mini, maxi)
            
            