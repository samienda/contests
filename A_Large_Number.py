t = int(input())


for _ in range(t):
    n, k = map(int, input().split())

    a = list(input())

# print(a[n-1:-1:-1])

    idx = n
    for i in range(n):
        if str(k) > a[i]:
            idx = i
            break 
        
    # print(low, high)
    a.insert(idx, str(k))
    
    print("".join(a))
