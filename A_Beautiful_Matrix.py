matrix = [list(map(int, input().split())) for _ in range(5)]

for row in range(5):
    if 1 in matrix[row]:
        col = matrix[row].index(1)
        x = abs(2 - col)
        y = abs(2 - row)
        print(x + y)
        break
