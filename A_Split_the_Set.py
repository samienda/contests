t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    odd = 0
    for num in array:
        if num % 2 :
            odd += 1
            
    print("Yes" if n == odd else "No")