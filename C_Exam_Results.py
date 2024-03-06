n  = int(input())

score = list(map(int, input().split()))
score.sort()
# print(score)

left = 0
found = False
for right in range(1,n):
    if found and score[right] > score[right - 1]:
        found = False
        score[left], score[right] = score[right], score[left]
        continue
        
        
    if not found and score[right] <= score[right - 1]:
        found = True 
        left = right
        

count = 0
for i in range(n - 1):
    if score[i] < score[i + 1]:
        count += 1
        
print(count)