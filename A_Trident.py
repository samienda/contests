t = int(input())

for _ in range(t):
    
    n = int(input())
    p = list(map(int, input().split()))
    
    stack = []
    
    
    for k in range(n):
        if len(stack) > 1 and p[stack[-1]] > p[k]:
            j = stack.pop() + 1
            i = stack.pop() + 1
            print("YES")
            print(i, j, k + 1)
            break 
        
        while stack and p[stack[-1]] > p[k]:
            stack.pop()
            
        stack.append(k)
    else:
        print('NO')
        
    
        
        