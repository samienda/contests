t = int(input())

def merge(left, right):
    
    if left[0] > right[0]:
        return right + left, 1
    return left + right, 0

def divide(left, right, nums):
    if right - left < 1:
        return nums[left: right + 1], 0
    
    mid = (left + right) // 2
    leftside, operleft = divide(left, mid, nums)
    rightside, operright = divide(mid + 1, right, nums)
    
    midside, mid =  merge(leftside, rightside)
    return midside, operleft + operright + mid


for _ in range(t):
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    improved, oper = divide(0,  n - 1, nums)
    # print(improved, oper)
    
    
    for i in range(1, n):
        if improved[i] < improved[i - 1]:
            print(-1)
            break
    else:
        print(oper)
        
    
    