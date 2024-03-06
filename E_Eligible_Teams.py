t = int(input())

for _ in range(t):
    
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    teams = 0
    left = 0
    for right in range(n):
        
        size = right - left + 1
        if size >= x / a[right]:
            left = right + 1
            teams += 1
            
    print(teams)
        
       