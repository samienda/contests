t = int(input())


def func(row, col, n, m, mat):
    x, y = row, col
    
    curr = 0
    while 0 <= x - 1 < n and  0 <= y - 1 < m:
        x -= 1
        y -= 1    
        curr += mat[x][y]
    
    x, y = row, col
    while 0 <= x - 1 < n and  0 <= y + 1 < m:
        x -= 1
        y += 1    
        curr += mat[x][y]
    
    x, y = row, col
    while 0 <= x + 1 < n and  0 <= y + 1< m:
        x += 1
        y += 1    
        curr += mat[x][y]
    
    x, y = row, col
    while 0 <= x + 1 < n and  0 <= y - 1 < m:
        x += 1
        y -= 1    
        curr += mat[x][y]
    
    return curr + mat[row][col]
    
    
    
    
    
    
    
    


for _ in range(t):
    n, m = list(map(int, input().split()))
    
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
        
    maxi = 0    
    for row in range(n):
        for col in range(m):
            maxi = max(maxi, func(row, col, n, m , mat))
    
    print(maxi)