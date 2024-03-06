t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    mat = []
    for x in range(n):
        mat.append(list(map(int, input().split())))
    
    swap = False
    row , col = 1, 1
    for i in range(n):
        mini = i
        for j in range(i, m): 
            if mat[i][j] > mat[i][mini]:
                mini = j
        if swap:
            print(-1)
            break
        swap = True

        row, col = j, j + 1
        for k in range(n):
            mat[k][i] , mat[k][mini] = mat[k][mini] , mat[k][i]
                    
    else:            
        print(row, col)
    