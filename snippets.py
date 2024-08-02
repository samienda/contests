
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