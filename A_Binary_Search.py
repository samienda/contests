n, k = map(int, input().split())
import bisect

a = list(map(int, input().split()))
q = list(map(int, input().split()))

for num in q:
    left = bisect.bisect_left(a, num)
    
    if 0 <= left < n and a[left] == num:
        print('YES')
    else:
        print('NO')
