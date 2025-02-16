n = int(input())


word = input()

answer = []

count = 0
for ch in word:

    if ch == 'W':
        if count > 0:
            answer.append(count)
        count = 0
    else:
        count += 1

if count > 0:
    answer.append(count)

print(len(answer))
print(*answer)
