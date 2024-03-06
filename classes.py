nums = [3, 2, 9, 4, 1, -2]
n = 6

running = 0
k = 2
for i in range(n):
    nums[i] = nums[i] * (k ** i)
    
    running += nums[i]
    nums[i] = running
    
print(nums)

ans = nums[4] - nums[1]
ans //= (k ** 2)
print(ans)


