def find(mat):
    target = ''
    row, col = 0, 0
    for i in range(n):
        for j in range(m):

            if mat[i][j] in ['S', 'T']:
                row, col = i, j

                if mat[i][j] == 'S':
                    target = 'T'
                else:
                    target = 'S'
                return row, col , target
            
            

def func(mat, row, col, target, n, m, dic):
    x, y = row, col
    while y <  m and mat[x][y] != '*': # go right after check
        
        r, c = x, y
        found = False
        while r + 1 < n and mat[r + 1][c] != '*' and not found: # go down
            r += 1
            
            if target in dic[r]:
                idx = mat[r].index(target)
                
                if idx  > c : # go right
                  while  c + 1 < m and mat[r][c + 1] != '*':
                      c += 1
                      if mat[r][c] == target:
                          return True
                
                elif idx  > c : # go left
                  while  c - 1 < m and mat[r][c - 1] != '*':
                      c -= 1
                      if mat[r][c] == target:
                          return True
                else:
                    return True
                
                found = True
            
                
        y += 1
        
        
    
        
    x, y = row, col
    while y - 1 >=  0 and mat[x][y - 1] != '*': # go left
        y -= 1
        
        r, c = x, y
        flag = False
        while r + 1 < n and mat[r + 1][c] != '*' and not flag: # go down
            r += 1
            if target in dic[r]:
                idx = mat[r].index(target)
                
                if idx  > c : # go right
                  while  c + 1 < m and mat[r][c + 1] != '*':
                      c += 1
                      if mat[r][c] == target:
                          return True
                
                elif idx  > c : # go left
                  while  c - 1 < m and mat[r][c - 1] != '*':
                      c -= 1
                      if mat[r][c] == target:
                          return True
                else:
                    return True
                
                flag = True
                
                


a  = list(map(int, input().split()))
n, m = a
mat = []
for _ in range(n):
    x = input()
    res = []
    for xi in x:
        res.append(xi)
    mat.append(res)

mat2 = [list(row) for row in zip(*mat)]


from collections import defaultdict
dic1 = defaultdict(set)
dic2 = defaultdict(set)

mx = max(n, m)
for i in range(n):
    for j in range(m):
        dic1[i].add(mat[i][j])
        dic2[j].add(mat2[j][i])





row1, col1, target1 = find(mat)
row2, col2, target2 = find(mat2)

if func(mat, row1, col1, target1, n, m, dic1) or func(mat2, row2, col2, target2, m, n, dic2):
    print("YES")
else:
    print("NO")   