t = int(input())
for _ in range(t):
    
    n, k = list(map(int, input().split()))
    
    
    answer = ""
    for i in range(k):
        
        for j in range(n // k):
            answer += chr(ord('a') + i)
            
    
    for i in range(n - len(answer)):
        answer += chr(ord('a') + i)
        
    print(answer)

lass UnionFind:
 def __init__(self, size):
 self.root = [i for i in range(size)]
 self.size = [1] * size
 def find(self, x):
 if x == self.root[x]:
 return x
 self.root[x] = self.find(self.root[x])
 return self.root[x]
 
 def union(self, x, y):
 rootX = self.find(x)
 rootY = self.find(y)
 if rootX != rootY:
 if self.size[rootX] > self.size[rootY]:
 self.root[rootY] = rootX
 self.size[rootX] += self.size[rootY]
 else:
 self.root[rootX] = rootY
 self.size[rootY] += self.size[rootX]
# Union by Size with Path Compression
# ● O(find) = amortized O(1)
# ● O(union) = amortized O(1)
# ● O(constructor) = O(V)
# Proof
class UnionFind:
 def __init__(self, size):
 self.root = [i for i in range(size)]
 self.size = [1] * size
 def find(self, x):
 if x == self.root[x]:
 return x
 self.root[x] = self.find(self.root[x])
 return self.root[x]
 
 def union(self, x, y):
 rootX = self.find(x)
 rootY = self.find(y)
 if rootX != rootY:
 if self.size[rootX] > self.size[rootY]:
 self.root[rootY] = rootX
 self.size[rootX] += self.size[rootY]
 else:
 self.root[rootX] = rootY
 self.size[rootY] += self.size[rootX]
P