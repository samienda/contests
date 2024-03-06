t = int(input())


polycarp = 'Yes' * 100

for _ in range(t):
    s = input()
    
    if s in polycarp:
        print('YES')
    else:
        print('NO')