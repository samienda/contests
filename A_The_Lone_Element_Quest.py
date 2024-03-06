t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    dis = set()
    for i in range(n):
        if a[i] not in a[i + 1:] + a[:i] :
            print(i + 1)
            break  
    