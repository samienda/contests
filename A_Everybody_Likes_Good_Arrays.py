t = int(input())


for _ in range(t):
    
    n = int(input())
    
    array = list(map(int, input().split()))
    
    stack = []
    count = 0
    for num in array:
        if stack and stack[-1] == num:
            stack.append(num * stack.pop())
            count += 1
        else:
            stack.append(num)
            
    print(count)
            
        
        