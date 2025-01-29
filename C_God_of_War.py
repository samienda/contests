t = int(input())


def calc(item):
    return item[0] + item[0] / item[-1]


def valid(value):

    for start, end in needed:
        if value < start:
            return False

        value += (end - start)

    return True


for _ in range(t):

    n = int(input())

    caves = []

    for i in range(n):
        caves.append(list(map(int, input().split())))

    needed = []
    for cave in caves:
        current = 0
        for j in range(1, len(cave)):
            if current <= cave[j]:
                current = cave[j] + 1

            current += 1

        needed.append([current - cave[0], current])

    needed.sort(key=calc)

    # needed.sort()

    low = 1
    high = 10 ** 10

    while low < high:
        mid = (low + high) // 2

        if valid(mid):
            high = mid
        else:
            low = mid + 1

    # print(needed)
    print(high)
