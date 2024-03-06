n = int(input())
nums = list(map(int, input().split()))
from collections import defaultdict
freq = defaultdict(int)
even  = 'even'
odd = 'odd'


freq[even] += 1

postive = 0
negative = 0
running = 0
for i in range(n):
    if nums[i] < 0:
        running += 1
        
    nums[i] = running
    
    
    if running % 2 == 0:
        postive += freq[even]
        negative += freq[odd]
        freq[even] += 1
    else:
        postive += freq[odd]
        negative += freq[even]
        freq[odd] += 1
        
print(negative, postive)