

t = int(input())

for _ in range(t):
    
    k = int(input())
    total = 100
    
    while k % 2 ==0 and total % 2 == 0:
        k //= 2
        total //= 2
         
    while k % 5 ==0 and total % 5 == 0:
        k //= 5
        total //= 5
        
    print(total) 