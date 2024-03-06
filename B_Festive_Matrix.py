n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))


sums = 0

for i in range(n):
    for j in range(n):
        if i - j == 0:
            sums += mat[i][j]
        elif i + j == n - 1:
            sums += mat[i][j]
        elif i == (n // 2) or j ==  (n//2):
            sums += mat[i][j]
            
            
print(sums)