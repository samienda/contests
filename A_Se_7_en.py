import bisect
t = int(input())
check = [14, 21, 28, 35, 42, 49, 56, 63, 77, 84, 91, 98, 105, 112, 119, 126, 133, 147, 154, 161,
         168, 175, 182, 189, 196, 203, 217, 224, 231, 238, 245, 252, 259, 266, 273, 287, 294, 301,
         308, 315, 322, 329, 336, 343, 357, 364, 371, 378, 385, 392, 399, 406, 413, 427, 434, 441,
         448, 455, 462, 469, 476, 483, 497, 504, 511, 518, 525, 532, 539, 546, 553, 567, 574, 581,
         588, 595, 602, 609, 616, 623, 637, 644, 651, 658, 665, 672, 679, 686, 693, 707, 714, 721,
         728, 735, 742, 749, 756, 763, 777, 784, 791, 798, 805, 812, 819, 826, 833, 847, 854, 861,
         868, 875, 882, 889, 896, 903, 917, 924, 931, 938, 945, 952, 959, 966, 973, 987, 994]


def find(n):
    idx = bisect.bisect_left(check, n)
    if idx >= len(check):
        idx -= 1

    f = str(check[idx])
    s = str(check[idx - 1])

    n = str(n)
    fc = 0
    sc = 0

    for i in range(len(n)):
        if i >= len(f):
            return s

        if n[i] != f[i]:
            break
        fc += 1

    for i in range(len(n)):
        if i >= len(s):
            return f

        if n[i] != s[i]:
            break
        sc += 1

    return s if fc < sc else f


for _ in range(t):

    n = int(input())
    print(find(n))

# print(find(989))
# print(find(779))
# print(find(19))
