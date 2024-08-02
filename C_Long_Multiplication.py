t = int(input())
for _ in range(t):
    x = list(input())
    y = list(input())
    
    n = len(x)
    # print(x)
    found = False
    for i in range(n):
        
        
        
        if not found:
            if x[i] < y[i]:
                x[i], y[i] = y[i], x[i]
                
            if x[i] > y[i]:
                found = True
        else:
            
            if x[i] > y[i]:
                x[i], y[i] = y[i], x[i]
            
            
        
    print("".join(x))
    print("".join(y))