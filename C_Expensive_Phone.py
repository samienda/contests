t = int(input())


for _ in range(t):
    
    n = int(input())
    
    a = list(map(int, input().split()))
    
    stack = []
    count = 0
    
    for num in a:
        while stack and stack[-1] > num:
            count += 1
            stack.pop()
            
        stack.append(num)
    
    print(count)