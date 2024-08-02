t = int(input())
from math import gcd



for _ in range(t):
    
    n = int(input())
    
    a = list(map(int, input().split()))
    
    primes = [True for _ in range(max(a) + 1)]
    d = 2
    while d ** 2 <= max(a):
        if primes[d]:
            j = d ** 2
            while j <= max(a):
                primes[j] = False
                j += d
        d += 1
        
    print(primes)
        
    a.sort()
    print(a)
    
    total = 0
    for i in range(n - 2):
        # if primes[i]:
        #     total += ()
        for j in range(i + 1, n -1):
            total += (gcd(a[i], a[j]) * (n - j - 1))
            
    print(total)
            