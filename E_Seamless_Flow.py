from collections import defaultdict
import copy

white = "white"
grey = "grey"
black = "black"


def dfs(node):
    
    color[node] = grey
    found = True
    for nbs in graph[node]:
        if color[nbs] == white:
            found = found and dfs(nbs)
        elif color[nbs] == grey:
            found = False
            
    color[node] = black
    return found
            

testcase = int(input())
for _ in range(testcase):

    n, m = map(int, input().split())

    graph = defaultdict(list)
    # graph = defaultdict(list)

    members = {}


    target = set()
    answer = []
    for _ in range(m):

        t, x, y = map(int, input().split())

        members[x] = white
        members[y] = white

        if t == 0:
            graph[x].append(y)
            graph[y].append(x)
            target.add((x, y))
        else:
            graph[x].append(y)
            answer.append([x, y])

    # print(target)
    # print(graph)
    
    can = True
    # print(answer)
    for x, y in target:
        color = copy.deepcopy(members)
        if dfs(x):
            answer.append([x, y])
            graph[y].remove(x)
            color = copy.deepcopy(members)
        elif dfs(y):    
            graph[x].remove(y)
            answer.append([y, x])
        else:
            can = False
            break
        
        
    print(answer if can else "NO")
            


