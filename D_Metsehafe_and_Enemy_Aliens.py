t = int(input())


for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    left = 0
    right = n - 1
    x = 0
    attack = 0
    count = n
    while left <= right:
        while x < a[right]:
            if x + a[left] > a[right]:
              amount = a[right] - x
              a[left] -= amount
              x += amount
              attack += amount
              
            else:  
                x += a[left]
                attack += a[left]
                a[left] = 0
                left += 1
                count -= 1
            print(x)
        
        print("xxxxxxxxxxxx", x)        
        a[right] -= x
        attack += 1
        x = 0
        right -= 1
        
        
    print("anser",attack)
                
            