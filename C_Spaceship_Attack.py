n, m = map(int, input().split())

s = list(map(int, input().split()))

base = [list(map(int, input().split())) for _ in range(m)]
base.sort()

for i in range(1, m):
    base[i][1] += base[i - 1][1]

import bisect
ans = []
# print(base)
for num in s:
    idx = bisect.bisect_right(base, [num, 10**10])
    if idx - 1 < 0:
        ans.append(0)
    else:
        ans.append(base[idx - 1][1])
    
print(*ans)