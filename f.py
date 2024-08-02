l, p, k = map(int, input().split())
signal = []
for _ in range(l):
    signal.append(input())

result = []
for line in signal:
    curr = ''
    for letter in line:
        curr += letter*k
    for _ in range(k):
        result.append(curr)
for i in result:
    print(i)