import heapq


heap = []
score = 0
for _ in range(int(input())):
    heapq.heappush(heap, (list(map(lambda itm : -int(itm), input().split()))[::-1]))
pick = 1
# print(heap)
while pick > 0 and heap:
    pick -= 1
    curr_pick, curr_score = heapq.heappop(heap) 
    score -= curr_score
    pick -= curr_pick
    # print(pick)
print(score)