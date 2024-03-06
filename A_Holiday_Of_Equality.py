n = int(input())

a = list(map(int, input().split()))


maxof = max(a)
totalspend = 0
for i in range(n):
    totalspend += maxof - a[i]

print(totalspend)
