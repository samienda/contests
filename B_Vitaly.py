n = int(input())

array = list(map(int, input().split()))

zero = []
neg = []
pos = []

for num in array:

    if num > 0 and not pos:
        pos.append(num)
    elif num < 0 and not neg:
        neg.append(num)
    else:
        zero.append(num)

if not pos:
    zero.sort(reverse=True)
    pos.append(zero.pop())
    pos.append(zero.pop())

print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)
