t = int(input())
for _ in range(t):
    x = int(input())
    y = bin(x)
    
    count = x.bit_count()
    
    # print(y, count)
    
    k = -1
    while k > - len(y) and y[k] == '0':
        k -= 1
        
    k += 1
    answer = 1<< (- k)
    
    if count == 1:
        answer += 1 if x != 1 else 2
        
    print(answer)
    