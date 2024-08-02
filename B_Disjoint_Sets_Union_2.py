n, q = list(map(int, input().split()))

parent =  [i for i in range(n + 1)]
size =  [1 for i in range(n + 1)]
mini =  [i for i in range(n + 1)]
maxi =  [i for i in range(n + 1)]

def find(x):
    if x == parent[x]:return x
    parent[x] = find(parent[x])
    return parent[x]


for _ in range(q):
    command = input().split()
    # print(command)
    
    if command[0] == "union":
        a = int(command[1])
        b = int(command[-1])
        
        roota = find(a)
        rootb = find(b)
        
        if roota != rootb:
            if size[roota] > size[rootb]:
                size[roota] += size[rootb]
                parent[rootb] = roota
                root = roota
            else:
                size[rootb] += size[roota]
                parent[roota] = rootb
                root = rootb
                
            mini[root] = min(mini[roota], mini[rootb])
            maxi[root] = max(maxi[roota], maxi[rootb])
    else:
        x = int(command[-1])
        rootx = find(x)
        print(mini[rootx], maxi[rootx], size[rootx])
        
        

        