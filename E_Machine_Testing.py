t = int(input())
from math import ceil

for _ in range(t):
    n = int(input())

    health = list(map(int, input().split()))
    power = list(map(int, input().split()))

    # print(health)
    # print(power)
    time = 0
    
    stack = [[power[0], 10**9]]
    ans = []
    
    if n == 1:
        print(0)
        continue
    
    for i in range(1, n):
        
        time = 0
        x = health[i]
        
        while x > 0:
            curr = stack[-1]
            
            if curr[0] * (curr[1] - time) >= x:
                time += ceil(x / curr[0])
                x = 0
            else:
                x -= (curr[0] * (curr[1] - time))
                time += (curr[1] - time)
                stack.pop()
        
        stack.append([power[i], time])
        # print(stack)  
                
        ans.append(time)
        
    # print(ans)
    
    print(max(ans))
            
        
        

