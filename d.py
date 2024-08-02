from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
test = int(input())

for _ in range(test):
    n, m, q = list(map(int, input().split()))
    time = list(map(int, input().split()))
    dictime = [[i, ch] for i, ch in enumerate(time)]
    dictime.sort(key= lambda x: x[-1])
    # print(time)
    # print(dictime)
    
    graph = defaultdict(list)
    
    for _ in range(m):
        
        u,v = list(map(int, input().split()))
        
        if time[u - 1] < time[v - 1]:
            graph[u].append(v)
        else:
            graph[v].append(u)
        
    # print(graph)
    
    queries = []
    for _ in range(q):
        s, d, t = list(map(int, input().split()))
        
        queries.append([t, s, d, _])
    
    queries.sort()
    # print(queries)
    answer = ["" for _ in range(q)]
    
    union = UnionFind(n+1)
    
    while queries:
        t, s, d, idx = queries.pop()
        
        levels = []
        while dictime and dictime[-1][-1] > t:
            i, node = dictime.pop()
            levels.append(i + 1)
            
        # print("levels", levels)
        for node in levels:
            for nbs in graph[node]:
                if time[nbs - 1] > t:
                    union.union(node, nbs)
                    
        roots = union.find(s)
        rootd = union.find(d)
        # print(union.root)
        found = False
        if rootd == roots:
            found = True
            
        if time[s - 1] > t:
            for nbs in graph[d]:
                rootnbs = union.find(nbs)
                if rootnbs == roots:
                    found = True
                    break
        answer[idx] = "YES" if found else "NO"
        
        
    for i in range(q):
        print(answer[i])
                    
                
                
        
        
        