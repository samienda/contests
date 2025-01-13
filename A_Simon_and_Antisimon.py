import math
a, b, n = list(map(int, input().split()))


turn = 's'
while n > 0:
    # print(n, turn)
    if turn == 's':
        x = math.gcd(a, n)
        # print(x)
        if x > n:
            print('1')
            break
        n -= x
        turn = 'a'
    else:
        x = math.gcd(b, n)
        # print(x, n)
        if x > n:
            print('0')
            break
        n -= x
        turn = 's'
else:
    print('1' if turn == 's' else '0')
