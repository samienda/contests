n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()


ptr1 = 0
ptr2 = 0
count = 0
# print(a)
# print(b)
while ptr1 < n and ptr2 < m:
    # print(a[ptr1], b[ptr2])
    if b[ptr2] in [a[ptr1], a[ptr1] + 1, a[ptr1] - 1]:
        count += 1
        ptr1 += 1
        ptr2 += 1
    else:
        if a[ptr1] + 1 > b[ptr2] :
            ptr2 += 1
        else:
            ptr1 += 1
            
print(count)

