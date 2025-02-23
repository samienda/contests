n = int(input())
result = []
for i in range(n):
    temp = []
    l, r = "C", "."
    if i % 2:
        l, r = r, l
    for j in range(n):
        if j % 2 == 0:
            temp.append(l)
        else:
            temp.append(r)
            
    result.append("".join(temp))
    
    
if n % 2 == 0:
    print((n // 2) * n)   
else: 
    print((((n // 2) + 1) ** 2) + ((n // 2) ** 2))

for i in result:
    print(i)