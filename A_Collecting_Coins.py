t = int(input())
for _ in range(t):
    a,b,c,n = list(map(int, input().split()))
    
    maxi = max(a,b,c)
    n -= (maxi - a)
    n -= (maxi - b)
    n -= (maxi - c)
    
    a = maxi
    b = maxi
    c = maxi
    
    if n >= 0 and n % 3 == 0:
        print("YES")
    else:
        print("NO")