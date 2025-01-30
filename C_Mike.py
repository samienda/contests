for _ in range(int(input())):
    n = int(input())
    b = input()
    prev = "0"
    a = []
    for i, itm in enumerate(b):
        if itm == "1":
            if prev == "2":
                a.append("0")
                prev = "1"
            else:
                a.append("1")
                prev = "2"
        else:
            if prev == "1":
                a.append("0")
                prev = "0"
            else:
                a.append("1")
                prev = "1"
    print("".join(a))                