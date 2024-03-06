s = input()
m = len(s)

n = int(input())

prefix = [0] * (m + 1)

for i in range(m - 1):
    if s[i] == s[i + 1]:
        prefix[i + 1] += 1
        
        
    prefix[i + 1] += prefix[i]

# print(prefix)
for _ in range(n):
    
    l, r = map(int, input().split())
    
    ans = prefix[r - 1] - prefix[l - 1]
    
    print(ans)
    