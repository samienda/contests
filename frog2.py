n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf') for _ in range(n)]
dp[0] = 0


for i in range(n):
  if dp[-1] > dp[i] or dp[i]:

    for j in range(1, k + 1):

        idx = i + j
        if idx < n:
            dp[idx] = min(dp[idx], dp[i] + abs(h[i] - h[idx]))
        else:
            break


print(dp[-1])
