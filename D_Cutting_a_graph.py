n, m, k = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

def find(x):
    if x == parent[x]:return x
    return find(parent[x])


for _ in range(m):
    a, b = list(map(int, input().split()))
    
queries = []

for _ in range(k):
    
    queries.append(list(map(str, input().split())))
    
answer = []
for t, a, b in reversed(queries):
    
    a = int(a)
    b = int(b)
    
    roota = find(a)
    rootb = find(b)
    
    if t == 'ask':
        answer.append("YES" if rootb == roota else "NO")
    else:
        if size[roota] > size[rootb]:
            parent[rootb] = roota
            size[roota] += size[rootb]
        else:
            parent[roota] = rootb
            size[rootb] += size[roota]
            
        
for ch in reversed(answer):
    print(ch)
    