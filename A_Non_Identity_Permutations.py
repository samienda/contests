t = int(input())
for _ in range(t):
    
    n = int(input())
    
    ans = [i for i in range(n, 0, -1)]
    # print(ans)
    
    if n % 2:
        ans[0], ans[n//2] = ans[n//2], ans[0]
        
    print(*ans)