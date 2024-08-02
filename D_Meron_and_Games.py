import sys
import threading

from collections import Counter


def main():
    n = int(input())

    array = list(map(int, input().split()))
    # array.sort()
    count = Counter(array)
    nums = list(count.keys())
    nums.sort(reverse=True)
    print(nums)
    print(count)

    memo = {}

    def move(idx, last):
        if idx >= len(nums):
            return 0

        state = (idx, last)
        if state not in memo:
            if last == -2 or last != nums[idx] + 1:
                memo[state] = max(
                    move(idx + 1, -2), move(idx + 1, nums[idx]) + (nums[idx] * count[nums[idx]]))
            else:
                memo[state] = move(idx + 1, -2)
        return memo[state]

    print(move(0, -2))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

