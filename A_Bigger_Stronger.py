t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    
    for i in range(n - 1):
        if a[i] in a[i + 1:]:
            print("NO")
            break
    else:
        print("YES")
        
        