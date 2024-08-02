t = int(input())

for _ in range(t):
    
    n, h = map(int, input().split())
    rope = []
    for _ in range(n):
        rope.append(list(map(int, input().split())))
        
    total = 0
    for w,l in rope:
        total += max(w, l)
        
    if total >= h:
        print("YES")
    else:
        print("NO")
        
    # print(rope)