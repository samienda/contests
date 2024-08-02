n = int(input())
array = list(map(int, input().split()))

left = 0
maxi = 1
for right  in range(1, n):
    
    if array[right - 1] >= array[right]:
        left = right
        
    
    maxi = max(maxi, right - left + 1)
    
print(maxi)
    