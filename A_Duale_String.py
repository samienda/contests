t = int(input())



for _ in range(t):
    s = input()
    n = len(s)
    if n % 2 != 0:
        print("NO")
        continue
    
    # print(n)
    for i in range(n//2):
        # print(i, i + (n // 2))
        if s[i] != s[i + (n // 2)]:
            print("NO")
            break
    else:
        print("YES")