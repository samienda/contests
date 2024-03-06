t = int(input())


dic = {}
for _ in range(t):
    
    name = input()
    if dic.get(name, 0) != 0:
        print(f'{name}{dic[name]}')
        dic[name] += 1
    else:
        dic[name] = 1 + dic.get(name, 0)
        print("OK")