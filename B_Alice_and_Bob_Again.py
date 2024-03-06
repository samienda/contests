t = int(input())


for _ in range(t):
    a = ""
    
    
    b = input()
    len_b = len(b)
    
    for i in range(len_b):
        if i % 2 == 0:
            a += b[i]
            
    if len_b % 2 == 0:
        a += b[len_b - 1]
    
    print(a)