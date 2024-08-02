from collections import Counter, defaultdict, deque


n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append(word)
    

    
incoming = Counter()
graph = defaultdict(list)

check = set()
impossible = False
for i in range(n - 1):
    m = len(words[i + 1])
    for j in range(len(words[i])):
        if j >= m or words[i][j] == words[i + 1][j]:
            continue
        
        a = words[i][j]
        b = words[i + 1][j]
        check.add(a)
        check.add(b)
        incoming[b] += 1
        incoming[a] += 0
        graph[a].append(b)
        break
    else:
        if len(words[i]) > m:
            impossible = True
            
if impossible:
    print("Impossible")
else:
    # print(check)
    # print(incoming)
    # print(graph)

    queue = deque()
    for i in incoming:
        if incoming[i] == 0:
            queue.append(i)
            
    answer =[]
    while queue:
        
        node = queue.popleft()
        answer.append(node)
        for nbs in graph[node]:
            
            incoming[nbs] -= 1
            if incoming[nbs] == 0:
                queue.append(nbs)
                
    # print(answer)
    for i in range(26):
        if chr(i + ord('a')) not in check:
            answer.append(chr(i + ord('a')))
            
    if len(answer) == 26:
        print("".join(answer))
    else:
        print("Impossible")