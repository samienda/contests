n = int(input())

s = input()


if 'YY' in s or 'MM' in s or 'CC' in s:
    print('No')
elif '??' in s or 'Y?Y' in s or 'C?C' in s or  'M?M' in s or '?' in [s[0], s[n - 1]]:
    print('Yes')
else:
    print('No')