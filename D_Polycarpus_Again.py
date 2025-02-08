from collections import Counter


r = input()


b, s, c = list(map(int, input().split()))
bprice, sprice, cprice = list(map(int, input().split()))
money = int(input())

counter = Counter(r)
# print(counter)

def valid(k):
    # print(k)
    bneed = (counter['B'] * k) - b
    if bneed > 0:
        bneed *= bprice
    else:
        bneed = 0

    sneed = (counter['S'] * k) - s
    if sneed > 0:
        sneed *= sprice
    else:
        sneed = 0

    cneed = (counter['C'] * k) - c
    if cneed > 0:
        cneed *= cprice
    else:
        cneed = 0
    # print(bneed, cneed, sneed, k)
    return cneed + bneed + sneed <= money


low = 0
high = 10 ** 14
count = 0
lastmid = 0
while low  <= high:
   
    
    # print(low, high)
    mid = (low + high) // 2
    
    

    if valid(mid):
        low = mid + 1
    else:
        high = mid - 1

print(low-1)
