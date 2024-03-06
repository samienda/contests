from collections import defaultdict
t = int(input())

for _ in range(t):
    
    n = int(input())
    
    a = list(map(int, input()))
    
    running = 0
    freq = defaultdict(int)
    # freq[0] += 1
    count = 0
    
    for i in range(n):
        store = running - i 
        running += a[i]
        
        check = running - i - 1
        
        freq[store] += 1
        count += freq[check]
        
    print(count)
        