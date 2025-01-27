

t = int(input())


target = 'bugyrt'


def compare(ch):
    if ch in target:
        return target.index(ch)
    return -1


for _ in range(t):
    n = int(input())

    a = list(input())
    print("".join(sorted(a, key=compare)))


print(sorted('lrud'))
