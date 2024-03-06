t = int(input())


for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    dic = {}
    
    
    for i in range(n):
        ai = a[i]
        dic[ai] = 1 + dic.get(ai, 0)
        
        if dic[ai] >= 3:
            print("YES")
            break
        elif dic[ai] >= 2:
            if i <= n - 2 and ai in a[i + 2:]:
                print("YES")
                break
            if i >= 2 and ai in a[:i - 1]:
                print("YES")
                break
        
    else:
        print("NO")        
    
                
        
        
        
    
        
        
  