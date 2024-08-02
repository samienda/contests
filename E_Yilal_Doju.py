n = int(input())
import math

a = list(map(int, input().split()))

res = []

def func1(a, b):
    if a > 2 * b:
        return math.ceil(a/2) 
    
    x = math.ceil((2 * a - b) / 3)
    total = x +  math.ceil(abs(b - x)/ 2)
    
    return total
    
def func2(a, b):
    total = b + (a - b) / 2
    
    return math.ceil(total)
    
    
for i in range(1, n):
    
    left = a[i - 1]
    mid = a[i]
    if i < n - 1:
        right = a[i + 1]
        res.append(func1(max(right, mid), min(right, mid)))
        res.append(func2(max(left, right), min(left, right)))
    
    res.append(func1(max(left, mid), min(left, mid)))
    
    
a.sort()
    
res.append(math.ceil(a[0]/2) + math.ceil(a[1]/2))

print(min(res))    