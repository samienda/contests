from collections import Counter


t = int(input())


for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    count = Counter(a)
    answer = set()
    for i in range(n):
        
        if count[a[i]] == 1:
            answer.add((a[i], i + 1))
            
    if answer:
        print(sorted(answer)[0][-1])
    else:
        print(- 1)
        