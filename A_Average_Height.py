t = int(input())


for _ in range(t):
    odd = []
    even = []
    n = int(input())
    nums = list(map(int, input().split()))
    
    
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    print(*odd, *even)
        
        