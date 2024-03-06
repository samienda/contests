n, k = map(int, input().split())

a = input()

aleft = 0
bleft = 0
ka = kb = k

for right in range(n):
    if a[right] == 'a':
        kb -= 1
    else:
        ka -= 1
        
        
    if ka < 0:
        if a[aleft] == 'b':
            ka += 1
        aleft += 1
        
    if kb < 0:
        if a[bleft] == 'a':
            kb += 1
        bleft += 1
        
print(max(n - aleft, n - bleft))
        