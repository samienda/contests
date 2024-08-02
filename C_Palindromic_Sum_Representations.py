

t = int(input())


def ispalidrome(s):
    return s == s[::-1]


palindromes = [i for i in range(1, 4 * 10 ** 4 + 2) if ispalidrome(str(i))]
dp = [0 for i in range(4 * 10 ** 4 + 2)]
dp[0] = 1
print(dp)
# for p in palindromes:

#     for i in range(4 * 10 ** 4 + 2):
#         idx = i - p
#         if idx >= 0:
#             dp[i] += dp[idx]

for _ in range(t):
    n = int(input())

    print(dp[n] % (10 ** 9 + 7))
