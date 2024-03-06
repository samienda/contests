t = int(input())


for _ in range(t):
    n = int(input())
    
    
    a = list(map(int, input().split()))
    count = 0
    dic = {}
    for i in range(n):
        count += dic.get(a[i] - i, 0)
        dic[a[i] - i] = 1 + dic.get(a[i] - i, 0)
            
            
    print(count)