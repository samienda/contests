t = int(input())


def check(array, grid, n):

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # print(i, j, (array[i] | array[j]))
            if grid[i][j] != (array[i] | array[j]):
                return False
    return True


for _ in range(t):

    n = int(input())

    grid = []
    for __ in range(n):
        grid.append(list(map(int, input().split())))

    # print(grid)

    answer = [2**30 - 1 for i in range(n)]
    # print(bin(2**30 - 1))

    for i in range(n):
        for j in range(n):
            if i != j:
                answer[i] &= grid[i][j]
                answer[j] &= grid[i][j]
        # print(answer)
    valid = check(answer, grid, n)
    if valid:
        print("YES")
        print(*answer)
    else:
        print("NO")