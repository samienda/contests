

from collections import deque


t = int(input())

for _ in range(t):

    n = int(input())
    alice = 0
    bob = 0

    add = 1

    turn = deque(['a', 'b'])
    while n > 0:

        node = turn.popleft()

        if node == 'a':
            if n > add:
                alice += add
                n -= add
            else:
                alice += n
                n = 0
            turn.append('b')
        else:
            if n > add:
                bob += add
                n -= add
            else:
                bob += n
                n = 0
            turn.append('a')

        add += 1

    print(alice, bob)
