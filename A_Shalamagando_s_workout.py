n = int(input())
array = list(map(int, input().split()))
each = {"chest":0, "biceps":0, "back":0}

for i in range(0, n, 3):
    each["chest"] += array[i]
    
    
for i in range(1, n, 3):
    each["biceps"] += array[i]
    
    
for i in range(2, n, 3):
    each["back"] += array[i]
    
    
maxi = sorted(each.items(), key=lambda item:item[1])[-1]

print(maxi[0])
    