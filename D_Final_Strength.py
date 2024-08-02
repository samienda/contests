
from copy import deepcopy
t = int(input())


def merge(lefthalf, righthalf):

    currlefthalf = deepcopy(lefthalf)
    currrighthalf = deepcopy(righthalf)

    right = 0
    for i in range(len(lefthalf)):

        while right < len(righthalf) and currlefthalf[i][0] > currrighthalf[right][0]:
            right += 1

        lefthalf[i][0] += right

    left = 0
    for i in range(len(righthalf)):

        while left < len(righthalf) and currrighthalf[i][0] > currlefthalf[left][0]:
            left += 1

        righthalf[i][0] += left

    left = 0
    right = 0
    newlis = []
    while left < len(lefthalf) and right < len(righthalf):
        if lefthalf[left][0] > righthalf[right][0]:

            newlis.append(righthalf[right])
            right += 1

        else:

            newlis.append(lefthalf[left])
            left += 1

    while left < len(lefthalf):
        newlis.append(lefthalf[left])
        left += 1

    while right < len(righthalf):
        newlis.append(righthalf[right])
        right += 1

    # print(lefthalf, righthalf)
    # print(newlis)
    return newlis


def divide(left, right, nums):
    if left >= right:
        return [nums[left]]

    mid = (left + right) // 2

    lefthalf = divide(left, mid, nums)
    righthalf = divide(mid + 1, right, nums)

    return merge(lefthalf, righthalf)


for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    b = [[num, i] for i, num in enumerate(a)]
    # print(b)
    ans = divide(0, len(a) - 1, b)
    ans.sort(key=lambda item: item[1])
    print(*[num for num, i in ans])
