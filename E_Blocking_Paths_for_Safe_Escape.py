t = int(input())


directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]


for _ in range(t):
    n, m = list(map(int, input().split()))
    def inbound(row, col): return 0 <= row < n and 0 <= col < m

    grid = [list(input()) for _ in range(n)]
    goodpeople = []

    # print(grid)

    posible = True
    for row in range(n):
        for col in range(m):

            if grid[row][col] == 'G':
                goodpeople.append((row, col))

            elif grid[row][col] == 'B':
                if (
                    row in [n - 1, n - 2]
                    and col in [m - 1, m - 2]
                ):
                    posible = False

                for r, c in directions:
                    newrow = row + r
                    newcol = col + c

                    if inbound(newrow, newcol):
                        
                        if grid[newrow][newcol] == 'G':
                            posible = False
                        elif grid[newrow][newcol] == '.':
                            grid[newrow][newcol] = '#'

    if not goodpeople:
        print('Yes')
        continue

    if not posible:
        print('No')
        continue
    # print(posible, grid)
    # print(goodpeople)
    for good in goodpeople:

        stack = [good]
        visted = [[False for j in range(m)] for i in range(n)]

        # print('stack', stack)
        while stack:

            row, col = stack.pop()

            if (row, col) == (n - 1, m - 1):
                posible = posible and True
                break

            visted[row][col] = True
            for r, c in directions:
                newrow = row + r
                newcol = col + c

                if (
                    inbound(newrow, newcol)
                    and not visted[newrow][newcol]
                    and grid[newrow][newcol] != '#'
                ):
                    stack.append((newrow, newcol))

            # print('stack', stack)
        else:
            posible = posible and False

    # print(posible, grid)

    if posible:
        print('Yes')
    else:
        print('No')
