n = int(input())
m = int(input())

a = []
for _ in range(n):
    a.append(int(input()))
    
a.sort(reverse=True)


for i in range(n):
    m -= a[i]
    
    if m <= 0:
        print(i + 1)
        break
    

