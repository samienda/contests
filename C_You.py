q = int(input())

for _ in range(q):
    
    n = int(input())
    
    x = n // 4
    r = n % 4
    possible = [0, 6, 9 , 15]
    
    
    while x > 0 and r not in possible:
        
        x -= 1
        r += 4
        
    
    # print(x, r)
    answer = x
    if r in [6, 9]:
        answer += 1
    elif r == 15:
        answer += 2
    print(answer if answer > 0 else -1)
    
    