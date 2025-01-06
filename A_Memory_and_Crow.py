n = int(input())


array = list(map(int, input().split()))

answer = array[:]


neg = 0
pos = 0

for  i in range(n - 1, -1, -1):
    if i % 2:
        answer[i] += neg
    else:
        answer[i] += pos
    
    if i % 2:
        neg += (- answer[i])
        pos += (answer[i])
    else:
        neg += ( answer[i])
        pos += ( - answer[i])
        
        
print(*answer)