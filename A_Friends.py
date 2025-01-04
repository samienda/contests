x = int(input())
y = int(input())
alast = 1
blast = 1


a = min(x, y)
b = max(x, y)
cost = 0
while a < b:
    # print(a, b, alast, blast)
    if alast < blast:
        cost += alast
        a += 1
        alast += 1
    else:
        cost += blast
        b -= 1
        blast += 1

print(cost)
