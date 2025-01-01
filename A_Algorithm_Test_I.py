from collections import Counter


m  = int(input())

a = list(map(int, input().split()))

count = Counter(a)

ans = 1
for i in range(1, len(count) + 1):
    ans *= i
    
print(ans)
    