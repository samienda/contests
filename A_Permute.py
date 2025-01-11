t = int(input())

for _ in range(t):

    n = int(input())
    array = list(map(int, input().split()))

    
    mini = 1
    maxi = len(array)
    
    if array == sorted(array):
        print(0)
    elif array[0] == mini and array[-1] == maxi:
        print(1)
    elif array[-1] == mini and array[0] == maxi:
        print(3)
    elif array[0] == mini:
        print(1)
    elif array[-1] == maxi:
        print(1)
    else:
        print(2)
 
        