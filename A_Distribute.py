n = int(input())
array = list(map(int, input().split()))


array = [[num, i] for i, num in enumerate(array)]
array.sort()

right = -1
for i in range(n // 2):
    print(array[i][-1] + 1, array[right][-1] + 1)
    right -= 1