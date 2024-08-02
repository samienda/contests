t = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))

    have = 0
    for num in nums:
        
        while num % 2 == 0:
            num /= 2
            have += 1
            
    powers = []
    need = n - have
    for i in range(1, n + 1):
        
        
        count = 0
        while i % 2 == 0:
            i /= 2
            count += 1
        
        if count:
            powers.append(count)
            
    powers.sort(reverse=True) 
    # print(powers, need)    
            
        
    oper = 0
    for power in powers:
        
        if need > 0:
            need -= power
            oper += 1
            
    # print(oper, need, "  ==")
    if need > 0:
        print(-1)
    else:
        print(oper)             