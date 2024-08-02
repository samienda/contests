n, k = list(map(int, input().split()))
array = list(map(int, input().split()))

prefix = array[:]
for i in range(1, n):
    prefix[i] += prefix[i - 1]


ans = (k) * prefix[-1] + - sum(sorted(prefix[:len(prefix) - 1])[:k - 1])

print(ans)
