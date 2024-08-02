from collections import deque


n = int(input())

starti, startj = list(map(int, input().split()))
desi, desj = list(map(int, input().split()))


grid = [list(input()) for _ in range(n)]
visted = [[False for i in range(n)] for _ in range(n)]

directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
def inbound(row, col): return 0 <= row < n and 0 <= col < n
def postive(r, c): return (r < 0 and c < 0) or (r > 0 and c > 0)


# print(grid)
# print(visted)

check = False
for r, c in directions:
    newrow = desi + r
    newcol = desj + c
    if not inbound(newrow, newcol):
        continue
    
    check = check or grid[newrow][newcol] != '#'



    

if check:

    queue = deque()
    visted = set()
    queue.append((starti - 1, startj - 1, 0))
    visted.add((starti, startj))
    found = False
    count = 0
    while queue and not found:
        
        size = len(queue)
        for i in range(size):
            # count += 1

            row, col, distance = queue.popleft()
            # print(row, col, distance)
            if (row, col) == (desi - 1, desj - 1):
                final = distance
                found = True
                break

            for r, c in directions:
                if found:
                    break
                for i in range(1, n):
                    newrow = row + (r) * i
                    newcol = col + (c) * i
                    # print("check---", newrow, newcol)

                    if not inbound(newrow, newcol) or grid[newrow][newcol] == '#':
                        break

                    if (newrow, newcol, r / c) not in visted:
                        queue.append((newrow, newcol, distance + 1))

                        visted.add((newrow, newcol, r / c))

                    if (newrow, newcol) == (desi - 1, desj - 1):
                        final = distance + 1
                        found = True
                        break
    # print(count)
    print(final if found else -1)
else:
    print(-1)
    

