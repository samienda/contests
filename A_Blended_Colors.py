t = int(input())

for _ in range(t):
    n = int(input())
    first = input()
    second = input()
    
    for i in range(n):
        if first[i] != second[i] and first[i] + second[i] not in ['BG', 'GB']:
            print("NO")
            break
    else:   
        print("YES")
    