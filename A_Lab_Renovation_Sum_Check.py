n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
    
    
def check(row, col):
    answer = set()
    
    for i in range(n):
        for j in range(n):
            answer.add(grid[row][i] + grid[j][col])
            
    return grid[row][col] in answer

found = True
for row in range(n):
    
    for col in range(n):
        if grid[row][col] != 1:
            found = check(row, col)
            if not found:
                print('No')
                break
            
    if not found:break
else:
    print('Yes')    

    