from collections import Counter, deque


t = int(input())

for _ in range(t):

    n, k = list(map(int, input().split()))
    s = list(input())

    count = Counter()
    queue = deque()
    print(k, s)

    def dp(right, left):
        print(left, right, count)
        if right >= n:
            return True

        if right - left == k:

            if count['0'] != count['1']:
                return False

            count[s[left]] -= 1
            return dp(right, left + 1)

        if s[right] != '?':
            count[s[right]] += 1
            return dp(right + 1, left)

      
        count['1'] += 1
        s[right] = '1'
        print('one')
        one = dp(right + 1, left)
        s[right] = '?'
        count['1'] -= 1

        count['0'] += 1
        s[right] = '0'
        print('two')
        two = dp(right + 1, left)
        s[right] = '?'
        count['0'] -= 1

        print(one, two)
        return one or two

    print(dp(0, 0))
