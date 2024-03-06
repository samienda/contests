t = int(input())


for _ in range(t):
    n = int(input())
    
    s = input()
    
    for i in range(n-1):
        if s[i: i+2] in s[i+2:]:
            print("YES")
            break
    else:
        print("NO")