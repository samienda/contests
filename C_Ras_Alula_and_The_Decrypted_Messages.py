t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    b = input()
    word = input()
    target = 0
    for ch in word:
        target += (ord(ch))

    left = 0
    running = 0
    # print(target)
    for right in range(n):
        running += (ord(b[right]))

        if right - left + 1 >= m:
            if target == running:
                print("YES")
                break
            running -= (ord(b[left]))
            left += 1

    # print(running)
    else:
        print("NO")
