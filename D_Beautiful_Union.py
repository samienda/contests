t = int(input())
from collections import defaultdict, Counter


def find(arr):
    n = len(arr)
    freq = Counter()
    
    last = arr[0]
    left = 0
    for right in range(1, n):
        curr = arr[right]
        last = arr[left]
        
        if curr != last:
            freq[last] = max(freq[last], right - left)
            left = right
        
        # print(last, curr)
            
    freq[arr[-1]] = max(freq[arr[-1]], n - left)
            
    return freq
# print(find([1,2,2,2,2]))
        

for _ in range(t):
    
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count1 = find(a)
    count2 = find(b)
    
    count = count1 + count2
    
    count = sorted(count.items(), key=lambda item:item[1])
    
    # print(count1, count2)
    print(count[-1][1])