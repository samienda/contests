letter = input()

memo = {
    'A': [
        [5, 5],
        [1, 4],
        [4, 5],
        [3, 5],
        [2, 3],
        [4, 3]
    ],
    'V': [
        [3, 2],
        [1, 2],
        [3, 2],
    ],
    '2': [
        [4, 3],
        [1, 2],
        [2, 3],
        [4, 3],
    ]
}

if letter == 'S':
    answer = memo['2']

    for a, b in answer:
        print(a, b)
else:
    answer = memo[letter]

    for a, b in answer:
        print(a, b)
