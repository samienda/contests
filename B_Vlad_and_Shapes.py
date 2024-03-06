t = int(input())


for _ in range(t):
    
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    
    found = False
    for i in range(n):
        for j in range(n):
            
            if grid[i][j] == 1:
                if grid[i + 1][j] == grid[i][j + 1] == grid[i][j]:
                    print('SQUARE')
                else:
                    print('TRIANGLE')
                
                found = True
                break 
            
        if found:
            break
        
        
