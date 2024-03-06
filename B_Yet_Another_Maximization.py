
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n <= k:
        print(sum(a))
        continue
    
    score = 0
    for i in range(1, k + 1):
        
        j = i + k
        curr = a[i - 1]
        while j <= n:
            curr = max(curr, a[j - 1])
            j += k
            
        score += curr
        
    print(score)
            
        