from collections import Counter


t = int(input())


def check(word, target):
    i = 0
    j = 0
    expected = Counter()
    count = Counter()
    # print(word, target)
    while j < len(target) and i < len(word):
        
        if word[i] == target[j]:
            j += 1
            if count[word[i]] > expected[word[i]]:
                # print(i, j)
                return False
            expected[word[i]] += 1
        
        count[word[i]] += 1        
        i += 1
    # print(i, j)
    return j >= len(target)


for _ in range(t):
    word, target = list(map(str, input().split()))

    valid = check(word[::-1], target[::-1])
    print('YES' if valid else 'NO')