from collections import Counter, defaultdict
import copy


n = int(input())
words = set()
answer = 0
need = defaultdict(Counter)
for _ in range(n):
    word = input()

    count = Counter(word)
    res = set()

    for ch in set(word):
        if count[ch] % 2:
            res.add(ch)
            words.add(ch)

    test = copy.deepcopy(res)

    res = tuple(sorted(res))
    # print(word, res, need)

    if len(res) == 0:
        answer += need[0][tuple([])]

        for ch in words:
            if ch in test:
                continue

            test.add(ch)
            # print(tuple(sorted(test)))
            answer += need[1][tuple(sorted(test))]
            test.remove(ch)
    else:
        answer += need[len(res)][tuple(sorted(res))]
        # print(test)
        # print(f'before test {answer}')
        # print(test, res)
        # print(tuple(sorted(test)))
        for ch in res:
            test.remove(ch)
            # print(test)
            answer += need[len(res) - 1][tuple(sorted(test))]
            test.add(ch)

        for ch in words:
            if ch in test:
                continue

            test.add(ch)
            # print(test)
            answer += need[len(res) + 1][tuple(sorted(test))]
            test.remove(ch)

    # print(answer)
    need[len(res)][tuple(sorted(res))] += 1


# print(words)
print(answer)
