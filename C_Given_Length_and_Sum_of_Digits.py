m, s = list(map(int, input().split()))
total = s

maxi = []

for i in range(m):
    curr = 9 if s >= 9 else s
    s -= curr

    maxi.append(curr)

# print(maxi)

s = total

curr = 1 if s < 9 * (m - 1) else s - ((m - 1) * 9)
s -= curr

mini = [curr]
for i in range(1, m):
    curr = 0 if s < 9 * (m - i - 1) else s - ((m - i - 1) * 9)
    s -= curr
    mini.append(curr)

# print(mini)
left = sum(mini)
right = sum(maxi)
# print(left, right, total)

print(*["".join(map(str, mini)), "".join(map(str, maxi))] if left == right == total else [-1, -1])
