n = int(input())


nums = list(map(int, input().split()))

nums.sort(reverse=True)

odd = 0
lodd = 0
even = 0
codd = 0

for num in nums:
    if num % 2 == 0:
        even += num
    else:
        lodd = num
        codd += 1
        odd += num

if codd % 2 != 0:
    print(even + odd - lodd)
else:
    print(even + odd)
