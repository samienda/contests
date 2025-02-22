from collections import deque


n, m, k = list(map(int, input().split()))


grid = [list(input()) for _ in range(n)]
print(grid)


queue = deque()

for i in range(n):
    if queue:
        break
    for j in range(m):
        if grid[i][j] == 'X':
            queue.append((i, j))
            break

answer = []



def inbound(i, j): return 0 <= i < n and 0 <= j < m


s = ['D', 'L', 'R', 'U']
directions = [
    (1, 0),
    (0, -1),
    (0, 1),
    (1, 0)
]

path = []

row, col = queue.pop()
def dp(i, j, k):
    # print(row, col)
    if k <= 0:
        print(path)
        if (i, j) == (row, col):
            answer.append("".join(path))
            return True
        return False

    found = False
    for idx, num in enumerate(directions): 
        r, c = num
        nrow = i + r
        ncol = j + c

        if inbound(nrow, ncol) and grid[nrow][ncol] != '*':
            path.append(s[idx])
            found = found or dp(nrow, ncol, k - 1)
            path.pop()

    return True

print(row, col, k)
valid = dp(row, col, k)
print(valid)
print(answer)
