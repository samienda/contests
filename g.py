from collections import defaultdict


n = int(input())
board = []
for _ in range(n):
    board.append(input())

def valid(row, col):
    return 0 <= row < n and 0 <= col < n
memo = {}
def dfs(row, col, curr, prev):
    prev += board[row][col]
    curr += board[row][col]
    if row == col == n-1:
        # print(curr, curr[::-1])
        if curr == curr[::-1]:
            return 
        else:
            return 0
    res = 0
    if valid(row+1, col):
        res += dfs(row+1, col, curr)
    if valid(row, col+1):
        res += dfs(row, col+1, curr)
    return res

print(dfs(0,0,''))