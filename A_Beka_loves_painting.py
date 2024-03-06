t = int(input())


for _ in range(t):
    
    n = int(input())
    
    left = []
    right = []
    
    a = list(map(int, input().split()))
    
    
    running = 0
    seen = set()
    for i in range(n):
        if i == 0 or a[i] not in seen:
            running += 1
        seen.add(a[i])
        x = i + 1
        left.append(running - x  - 1)
        right.append(x - running)
       
    l = left.index(max(left))
    r = right.index(max(right))
    print(l + 1, r + 1)