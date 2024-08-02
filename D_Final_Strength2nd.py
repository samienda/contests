from collections import deque
t = int(input())


def merge(lefthalf, righthalf):

    leftscore = 0
    rightscore = 0

    leftqueue = deque(lefthalf)
    rightqueue = deque(righthalf)
    newlis = []

    while leftqueue and rightqueue:

        if leftqueue[0][0] < rightqueue[0][0]:

            newnum = leftqueue.popleft()
            newnum[0] += leftscore
            newlis.append(newnum)
            rightscore += 1

        elif leftqueue[0][0] > rightqueue[0][0]:

            newnum = rightqueue.popleft()
            newnum[0] += rightscore
            newlis.append(newnum)
            leftscore += 1

        else:

            xleft = leftscore
            xright = rightscore
            val = leftqueue[0][0]

            currlis = []
            while leftqueue and leftqueue[0][0] == val:

                newnum = leftqueue.popleft()
                newnum[0] += xleft
                currlis.append(newnum)
                rightscore += 1

            while rightqueue and rightqueue[0][0] == val:

                newnum = rightqueue.popleft()
                newnum[0] += xright
                currlis.append(newnum)
                leftscore += 1
            # print(currlis)
            for num in sorted(currlis):
                newlis.append(num)

    while leftqueue:
        newnum = leftqueue.popleft()
        newnum[0] += leftscore
        newlis.append(newnum)

    while rightqueue:
        newnum = rightqueue.popleft()
        newnum[0] += rightscore
        newlis.append(newnum)

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

    ans = divide(0, len(a) - 1, b)
    ans.sort(key=lambda item: item[1])
    print(*[num for num, i in ans])
