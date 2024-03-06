t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    left = 0
    right = n - 1
    found = False
    modification = []
    
    while left < right:
        if not found and s[left] != s[right]:
            found = True
            
        if found and s[left] != s[right]:
            modification.append(left)
            
        left += 1
        right -= 1
            
    # print(modification)
    for i in range(len(modification) - 1):
        if modification[i] + 1 != modification[i + 1]:
            print('No')
            break
    else:
        print('Yes')
            
    
    