from collections import defaultdict
n = int(input())

parent = [i for i in range(n + 1)]
rank = [0 for i in range(n + 1)]


def find(x):

    while x != parent[x]:

        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

memo = defaultdict(list)
for i in range(1, n + 1):
    memo[i].append(i)

for _ in range(n - 1):

    a, b = list(map(int, input().split()))
    roota = find(a)
    rootb = find(b)
    # print(memo)
    
    if rank[roota] > rank[rootb]:
    
        memo[roota].extend(memo[rootb])
        parent[rootb] = roota
        
    elif rank[roota] < rank[rootb]:
        
        memo[rootb].extend(memo[roota])
        parent[roota] = rootb
        
    else:      

        memo[roota].extend(memo[rootb])
        parent[rootb] = roota
        
        rank[roota] += 1

# print(memo)
for i in range(n + 1):
    parent[i] = find(roota)

print(*memo[parent[1]])
