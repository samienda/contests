n = int(input())

x = list(map(int, input().split()))
v = list(map(int, input().split()))

combined = [[x[i], v[i]] for i in range(n)]

combined.sort()
print(combined)

def calc(pos):
    
    ans = 0
    
    for d, s in combined:
        ans = max(ans, abs(d - pos) / s)
        
    return ans

 
