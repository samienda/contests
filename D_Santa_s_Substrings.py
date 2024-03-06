n = int(input())


mat = []
for _ in range(n):
    mat.append(input())
    
    
def compare(item):
    return len(item)


mat.sort(key=compare)


for i in range(n - 1):
    if mat[i] not in mat[i + 1]:
        print("NO")
        break
else:    
    print("YES")
    for m in mat:
        print(m)     