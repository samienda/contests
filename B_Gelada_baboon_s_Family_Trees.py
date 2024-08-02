n = int(input())
nodes = list(map(int, input().split()))

# n = len(nodes)
parent = [_ for _ in range(n + 1)]
# print(n)


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


for i in range(n):
    a = i + 1
    b = nodes[i]

    roota = find(a)
    rootb = find(b)

    parent[rootb] = roota

for i in range(n):
    parent[i + 1] = find(i + 1)

print(len(set(parent[1:])))

# print(len(set([])))