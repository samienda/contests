t = int(input())


for _ in range(t):
    n = int(input())
    s = input()
    target = 'abacaba'
    
    
    count = 0
    for i in range(n - 6):
        if s[i:i + 7] == target:
            count += 1
            
    if count == 1:
        s = s.replace('?', 'd')
        print('Yes')
        print(s)
        continue
    elif count > 1:
        print('No')
        continue
        
        
    
    for j in range(n - 6):
        curr = list(s)
        for x in range(j, j + 7):
            if curr[x] == '?':
                curr[x] = target[x - j]
        else:
            count = 0
            curr = ''.join(curr).replace('?', 'd')
            for p in range(n - 6):
                if curr[p:p + 7] == target:
                    count += 1
                    
            if count == 1:                        
                print('Yes')
                print(curr)
                break
    else:
        print('No')