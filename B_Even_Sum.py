t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)
    if total % 2 == 0:
        print(0)
        continue

    oper = float('inf')
    for num in a:
        y = num
        x = 0
        if num % 2 == 1:
            while num % 2 == 1:
                num //= 2
                # print(num)
                x += 1
            oper = min(
                oper, x
            )

        elif num % 2 == 0:
            while num > 1:
                num //= 2
                x += 1

            oper = min(
                oper, x
            )

    print(oper)
