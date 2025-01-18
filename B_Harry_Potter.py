n = input()

def add(n):
    
    ans = 0
    for num in n:
        ans += (int(num))
        
    return ans

count = 0
while len(n) > 1:
    
    x = add(n)
    n = str(x)
    count += 1
    
print(count)