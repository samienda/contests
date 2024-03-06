n = int(input())

show = [list(map(int, input().split())) for _ in range(n)]

show.sort()
# show.sort(key=lambda item:item[1])

one = -1
two = -1

# print(show)
for start, end in show:
    if start > one:
        one = end
    elif start > two:
        two = end
    else:
        print("NO")
        break
else:
    print("YES")
