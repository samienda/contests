t = int(input())


for _ in range(t):
    
    s = list(input())
    n = len(s)

    w = 0
    for i in range(n - 1):
        ch = s[i]
        if ch == 'v' and s[i + 1] == 'v':
            s[i + 1] = 'a'
            s[i] =  'a'
            w += 1
        elif ch == 'w':
            w += 1

    if s[n - 1] == 'w':
        w += 1
            
    print( w)
    