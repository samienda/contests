t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    a.sort()
    
    print(a[n - 1] - a[0])