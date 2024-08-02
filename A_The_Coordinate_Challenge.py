
def find(n):
    if n == 0:return 0
    if n == 1: return 2
    if n == 2: return 1
    
    if n == 4:
        return 2
    
    if n % 3 == 0:
        return find(n % 3) + n // 3
    
    if n % 3 == 1 and n > 3:
        return find(4) + (n - 4) // 3
    
    if n % 3 == 2 and n > 3:
        return find(2) + n // 3
    
     
    
    
    
t = int(input())
for _ in range(t):
    print(find(int(input())))
