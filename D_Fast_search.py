n = int(input())
import bisect

a = list(map(int, input().split()))
n = int(input())

a.sort()
ans = []
for i in range(n):
    l, r = list(map(int, input().split()))
    
    left = bisect.bisect_left(a, l)
    right = bisect.bisect_right(a, r)
    
    ans.append(right - left)
    
print(*ans)