from collections import deque


t = int(input())
for _ in range(t):
    
    s = input()
    ans = deque()
    
    for ch in reversed(s):
        ans.append(ch)
        ans.appendleft(ch)
        
    print("".join(ans))