from collections import Counter
t = int(input())


for _ in range(t):

    n = int(input())
    array = list(map(int, input().split()))

    count = sorted(Counter(array).items(),
                   key=lambda item: item[1], reverse=True)

    print(count[0][1])
