brack = input()
stack = []
count = 0
for b in brack:
    if b == ')':
        if stack:
            stack.pop()
            count += 2
    else:
        stack.append(b)
        
print(count)
            
        
        