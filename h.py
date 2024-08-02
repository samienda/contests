mapper = {('R', 'R'): "R", ('G', 'G'): "G", ('B', 'B'): "B", ('R', 'G'): "B", ('R', 'B'): "G", ('G', 'R'): "B", ('G', 'B'): "R", ('B', 'R'): "G", ('B', 'G'): "R", }
s = input()
prev = s
for i in range(len(s), 1, -1):
    curr = ''
    for j in range(i-1):
        curr += mapper[(s[j], s[j+1])]
    prev = curr
    # print(prev)
print(curr)
