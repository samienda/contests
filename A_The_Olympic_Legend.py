t = int(input())

for _ in range(t):
    k, *athletes = list(map(int, input().split()))
    count = 0
    for athlete in athletes:
        if athlete > k:
            count += 1
            
            
    print(count)