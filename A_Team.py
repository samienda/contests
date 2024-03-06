q = int(input())

count = 0
for _ in range(q):
    soln = list(map(int, input().split()))

    if sum(soln) > 1:
        count += 1


print(count)
