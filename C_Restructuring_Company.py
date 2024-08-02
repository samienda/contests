n, q = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
rank = [0 for i in range(n + 1)]

type2parent = [i for i in range(n + 1)]


def find(x, parent):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]


for _ in range(q):
    t, x, y = list(map(int, input().split()))

    rootx = find(min(x, y), parent)
    rooty = find(max(x, y), parent)

    if t == 3:
        print("YES" if rootx == rooty else "NO")
    elif t == 2:
        if find(x, type2parent) != find(y, type2parent):
            # print("done")
            rooty2 = find(max(x, y), type2parent)
            for i in range(min(x, y) + 1, max(x, y) + 1):
                rooti = find(i, parent)
                rootj = find(i, type2parent)
                
                parent[rooti] = rootx
                type2parent[rootj] = rooty2
    else:
        if rank[rootx] < rank[rooty]:
            rank[rooty] += rank[rootx]
            parent[rootx] = rooty
        else:
            rank[rootx] += rank[rooty]
            parent[rooty] = rootx
