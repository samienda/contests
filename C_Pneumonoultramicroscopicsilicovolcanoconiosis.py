t = int(input())

for _ in range(t):

    word = input()
    n = len(word)

    if n > 10:
        first = word[0]
        last = word[n - 1]
        print(f'{first}{n - 2}{last}')
    else:
        print(word)
