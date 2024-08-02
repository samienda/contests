text1 = input()
text2 = input()
n = len(text1)
m = len(text2)

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

for i in range(n):
    for j in range(m):
        if text1[i] == text2[j]:
            dp[i + 1][j + 1] = 1 + dp[i][j]
        else:
            dp[i + 1][j + 1] =  max(dp[i + 1][j], dp[i][j + 1])

# print(dp)


row = n 
col = m
answer = []
while row > 0 and col > 0:
    
    if text1[row - 1] == text2[col - 1]:
        answer.append(text1[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1 
    else:
        col -= 1
        
print("".join(answer[::-1]))
        