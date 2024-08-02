from math import gcd


n = int(input())
a = list(map(int, input().split()))


greatest = gcd(*a)
# print(greatest)
for i in range(n):
    a[i] = a[i] // greatest

    while a[i] % 2 == 0:
        a[i] //= 2

    while a[i] % 3 == 0:
        a[i] //= 3


# print(a)

for i in range(n - 1):

    if a[i] != a[i + 1]:
        print('No')
        break

else:
    print('Yes')


# def calc(num):
#     curr = defaultdict(int)

#     d = 2
#     while d ** 2 < num:
#         while num % d == 0:
#             num //= d
#             if d not in [2, 3]:
#                 curr[d] += 1
#         d += 1

#     if num > 1 and num not in [2, 3]:
#         curr[num] += 1

#     return curr


# print(a)
# must = calc(a[0])

# for i in range(1, n):

#     if must != calc(a[i]):
#         print('No')
#         break
# else:
#     print('Yes')
