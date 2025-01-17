s = input()

k =int(input())

c = set(s)


if len(s) < k:
    print('impossible')
else:
    if len(c) < k:
        print(k - len(c))
    else:
        print(0)