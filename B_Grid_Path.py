

import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = list(map(int, input().split()))

        def inbound(row, col): return 0 <= row <= n and 0 <= col < m

        memo = {}

        def pick(i, j, target):
            if i == n - 1 and j == m - 1:
                return target == 0

            if not inbound(i, j):
                return False

            state = (i, j, target)
            if state not in memo:
                memo[state] = pick(i + 1, j, target - j -1) or pick(i, j + 1, target - i - 1)
            return memo[state]

        print("YES" if pick(0, 0, k) else "NO")


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
