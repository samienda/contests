t = int(input())

for _ in range(t):
    n = int(input())
    
    evencount = 0
    oddcount = 0
        
    if n % 2 != 0 :
        print("Yes")
        for i in range(n):
            if i < (n / 2): 
                print(i + 1, (2 * n) - evencount)
                evencount += 2
            else:
                print(i + 1, (2 * n) - oddcount - 1)  
                oddcount += 2
    else:
        print("No")
        