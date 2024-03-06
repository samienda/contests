from copy import deepcopy

t = int(input())


def func(n, mat):
    temp = [[0, 0], [ n - 1, 0], [ 0, n- 1] ,  [n - 1, n - 1]]
    updatein = [[0, 1], [-1, 0], [1, 0], [0, -1] ]
    updateout = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    
    oper = 0
    direction = deepcopy(temp)
    for _ in range(n//2):
        
        while direction[0][1] < direction[2][1] and direction[0][0] < direction[1][0] and direction[2][0] < direction[3][0] and direction[1][1] < direction[3][1]:
            dic = [0, 0]
            for k in range(4):
                x = direction[k]
                
                val = mat[x[0]][x[1]]
                dic[val] += 1
            
            oper += min(dic)
            
            
            for i in range(4):
                direction[i][0] += updatein[i][0]
                direction[i][1] += updatein[i][1]
        
        for j in range(4):
            temp[j][0] += updateout[j][0]
            temp[j][1] += updateout[j][1]
        direction = deepcopy(temp)  
        
    return oper
            
    
        





for _ in range(t):
    n = int(input())
    
    mat = []
    for _ in range(n):
        x = input()
        res = []
        for xi in x:
            res.append(int(xi))
        mat.append(res)
        
    print(func(n=n, mat=mat))
        
        
        

    