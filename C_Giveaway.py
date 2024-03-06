n, q = map(int, input().split())


p = list(map(int, input().split()))
p.sort()

for i in range(1, n):
    p[i] += p[i- 1]
    
# print(p)


for _ in range(q):
    x, y = map(int, input().split())    
    
    ans = p[n - (x - y) - 1] - p[n - x - 1]
    if x == n:
        ans = p[y - 1]
    print(ans)
    