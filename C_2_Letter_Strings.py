from collections import Counter, defaultdict
t = int(input())
zero = defaultdict(list)
one = defaultdict(list)

latin = 'abcdefghijk'

for _ in range(t):

    n = int(input())
    words = []
    together = Counter()
    count = 0
    for i in range(n):
        word = input()
        words.append(word)

        xword = []
        yword = []
        for ch in latin:
            x = word[0] + ch
            y = ch + word[1]

            if x != word:
                xword.append(x)
                count += together[x]

            if y != word:
                yword.append(y)
                count += together[y]

        # print(together)
        # print(word)
        # print(xword)
        # print(yword)
        # print(count)
        together[word] += 1

    print(count)

    #     count += len(zero[word[0]])
    #     count += len(one[word[1]])
    #     count -= (2 * together[word])

    #     zero[word[0]].append(word[1])
    #     one[word[1]].append(word[0])
    #     together[word] += 1

    # print('zero', zero)
    # print('one', one)

    # print(words, count)
