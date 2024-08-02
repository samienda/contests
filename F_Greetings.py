t = int(input())



def merge(lefthalf, righthalf):
    left = 0
    right = 0
    
    newlis = []
    count = 0
    curr = 0
    while left < len(lefthalf) and right < len(righthalf):
        if lefthalf[left][0] > righthalf[right][0]:
            curr += 1
            newlis.append(righthalf[right])
            right += 1
        else:
            newlis.append(lefthalf[left])
            left += 1
            count += curr
            
    while left < len(lefthalf):
        newlis.append(lefthalf[left])
        left += 1
        count += curr
            
    while right < len(righthalf):
        newlis.append(righthalf[right])
        right += 1

    # print(lefthalf, righthalf)
    # print( newlis, count)
    return newlis, count 

def divide(left, right, nums):
    if left == right:
        return [nums[left]], 0
    
    mid = (left + right) // 2
    
    lefthalf, leftcount = divide(left, mid, nums)   
    righthalf, rightcount = divide(mid + 1, right, nums)   

    combined, combinedcount =  merge(lefthalf, righthalf)

    return combined, leftcount + combinedcount + rightcount


for _ in range(t):
    
    n = int(input())
    
    nums = [ list(map(int, input().split())) for _ in range(n)]
    
    nums.sort(key=lambda item:item[1])
    # print(nums)
    
    nums, count = divide(0, n - 1, nums)
    
    # print(nums, count)
    print(count)
    
import random
print(random.randint(0,5))
    

    