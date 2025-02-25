

from collections import deque


# def can_reach_destination(grid, initial_gas):
#     rows = len(grid)
#     if rows == 0:
#         return False
#     cols = len(grid[0])
#     count = 0

#     # Find start, destination, and gas stations
#     start = None
#     dest = None
#     gas_stations = []
#     for i in range(rows):
#         for j in range(cols):
#             cell = grid[i][j]
#             if cell == 's':
#                 start = (i, j)
#             elif cell == 'd':
#                 dest = (i, j)
#             elif cell.isdigit():
#                 gas_stations.append((i, j, int(cell)))

#     if not start or not dest:
#         return False  # invalid grid

#     # Assign an index to each gas station for bitmasking
#     gas_station_indices = {(i, j): idx for idx, (i, j, _)
#                            in enumerate(gas_stations)}

#     print(gas_station_indices)
#     visited = {}  # key: (i, j, mask), value: max gas available
#     start_i, start_j = start
#     initial_mask = 0
#     queue = deque([(start_i, start_j, initial_gas, initial_mask)])
#     visited[(start_i, start_j, initial_mask)] = initial_gas

#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     while queue:
#         i, j, gas, mask = queue.popleft()
#         count += 1
#         print("currently at", i, j, "with gas", gas, "and mask", mask)

#         # Check if current position is the destination
#         if (i, j) == dest:
#             print("Destination reached at", i, j, "with gas", gas,
#                   "with iterations", count, "for grid", rows, "by", cols)
#             return True

#         for dx, dy in directions:
#             ni, nj = i + dx, j + dy
#             if 0 <= ni < rows and 0 <= nj < cols:
#                 cell = grid[ni][nj]
#                 # Skip blocked cells (assuming non-digit, non-s/d/* are blocked)
#                 if cell not in ('s', 'd', '*') and not cell.isdigit():
#                     continue

#                 # Check if we can move (need at least 1 gas)
#                 if gas < 1:
#                     continue
#                 new_gas = gas - 1
#                 new_mask = mask

#                 # Check if the new cell is a gas station not yet collected
#                 if (ni, nj) in gas_station_indices and cell.isdigit():
#                     idx = gas_station_indices[(ni, nj)]
#                     if not (mask & (1 << idx)):
#                         # Collect the gas station
#                         new_gas += gas_stations[idx][2]
#                         new_mask = mask | (1 << idx)

#                 # Check if this state is better than previously recorded
#                 state_key = (ni, nj, new_mask)
#                 if state_key not in visited or new_gas > visited.get(state_key, -1):
#                     if new_gas < 0:
#                         continue  # invalid state
#                     visited[state_key] = new_gas
#                     queue.append((ni, nj, new_gas, new_mask))

#     # Destination not reachable
#     return False


def can_reach_destination(grid, initial_gas):
    rows = len(grid)
    if rows == 0:
        return False
    cols = len(grid[0])
    count = 0
    # Find start, destination, and gas stations
    start = None
    dest = None
    gas_stations = {}
    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            if cell == 's':
                start = (i, j)
            elif cell == 'd':
                dest = (i, j)
            elif cell.isdigit():
                gas_stations[(i, j)] = int(cell)

    if not start or not dest:
        return False  # invalid grid

    # BFS setup
    visited = {}  # key: (i, j), value: max gas available at this cell
    start_i, start_j = start
    # (i, j, gas, visited_stations)
    queue = deque([(start_i, start_j, initial_gas, set())])
    visited[(start_i, start_j)] = initial_gas

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        i, j, gas, visited_stations = queue.popleft()
        # print("currently at", i, j, "with gas", gas,
        #       "visted stations", visited_stations)
        count += 1
        # Check if current position is the destination
        if (i, j) == dest:
            print("Destination reached at", i, j, "with gas", gas,
                  "with iterations", count, "for grid", rows, "by", cols)
            return True

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols:
                cell = grid[ni][nj]
                # Skip blocked cells (assuming non-digit, non-s/d/* are blocked)
                if cell not in ('s', 'd', '*') and not cell.isdigit():
                    continue

                # Check if we can move (need at least 1 gas)
                if gas < 1:
                    continue
                new_gas = gas - 1
                new_visited_stations = set(visited_stations)

                # Check if the new cell is a gas station not yet collected
                if (ni, nj) in gas_stations and (ni, nj) not in visited_stations:
                    new_gas += gas_stations[(ni, nj)]
                    new_visited_stations.add((ni, nj))

                # Check if this state is better than previously recorded
                state_key = (ni, nj)
                if state_key not in visited or new_gas > visited.get(state_key, -1):
                    if new_gas < 0:
                        continue  # invalid state
                    visited[state_key] = new_gas
                    queue.append((ni, nj, new_gas, new_visited_stations))

    # Destination not reachable
    print("Destination not reachable", "with iterations", count)
    return False


# Example usage
grid = [
    ['*', '*', '1', '*', '*', '*', '*', '*', '*', '*',
        '*', '*', '*', '*', 'd', '*', '1', '1', '1', '1'],
    ['*', '*', '*', '1', '*', '*', '*', '*', '*', '*',
        '*', '*', '*', '*', '*', '*', '1', '1', '1', '1'],
    ['*', '*', '*', '*', '*', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '*', '*', '*', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', '1', '*', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        '1', '1', '1', '1', 's', '*', '1', '1', '1', '1'],
]
initial_gas = 2
print(can_reach_destination(grid, initial_gas))  # Output: True



















# import sys
# import threading


# def input(): return sys.stdin.readline().strip()


# def main():
#     pass


# if __name__ == '__main__':

#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()


# UNION FIND BY SIZE


# class UnionFind:
#     def __init__(self, size):
#         self.root = [i for i in range(size)]
#         self.size = [1] * size

#     def find(self, x):
#         while x != self.root[x]:
#             self.root[x] = self.root[self.root[x]]
#             x = self.root[x]
#         return x

#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             if self.size[rootX] > self.size[rootY]:
#                 self.root[rootY] = rootX
#                 self.size[rootX] += self.size[rootY]
#             else:
#                 self.root[rootX] = rootY
#                 self.size[rootY] += self.size[rootX]


# UNION FIND BY RANK


# class UnionFind:
#     def __init__(self, size):
#         self.root = [i for i in range(size)]
#         self.rank = [0] * size

#     def find(self, x):
#         if x != self.root[x]:
#             self.root[x] = self.find(self.root[x])
#         return self.root[x]

#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)

#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.root[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.root[rootX] = rootY
#             else:
#                 self.root[rootY] = rootX
#                 self.rank[rootX] += 1


#  SOFI CODE FOR UNION FIND

# parent = {i:i for i in range(1, n+1)}
# rank = [0 for i in range(n+1)]

# def find(num):
#     while num != parent[num]:
#         parent[num] = parent[parent[num]]
#         num = parent[num]
#     return num

# def union(a, b):
#     # print(rank)
#     parent1 = find(a)
#     parent2 = find(b)


#     if parent1 != parent2:
#         if rank[parent1] > rank[parent2]:
#             parent[parent2] = parent1
#         elif rank[parent2] > rank[parent1]:
#             parent[parent1] = parent2
#         else:
#             parent[parent2] = parent1
#             rank[parent1] += 1


# Trie = lambda: defaultdict(TrieNode)
# trie = Trie()
# def insert(trie, word) -> None:
#     current = trie
#     for ch in word:
#         if not current.children[ch]:
#             current.children[ch] = Trie()
#         current = current.children[ch]
    
#     current["isEnd"] = True