t = int(input())

for _ in range(t):
    X = input()
    # num = list(map(int, X))
    
    num = int(X)
    
    while num % 2 == 0:
        num //= 2
        
    if num > 1:
        print('YES')
    else:
        print("NO")