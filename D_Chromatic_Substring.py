q = int(input())


for _ in range(q):
    n, k = map(int, input().split())
    b = input()
    a = list(b)
    
    val = 'RG  GB  BR'
    left = 0
    changed = set()
    changes = 0
    ans = []
    for right in range(n - 1):
        if a[right] == 'R' and a[right + 1] != 'G':
            a[right + 1] = 'G'
            changed.add(right + 1)
            changes += 1    
        elif a[right] == 'G' and a[right + 1] != 'B':
            a[right + 1] = 'B'
            changed.add(right + 1)
            changes += 1   
        elif a[right] == 'B' and a[right + 1] != 'R':
            a[right + 1] = 'R'
            changed.add(right + 1)
            changes += 1
            
        if right - left + 1 == k - 1:
            ans.append(changes)
            if left in changed:
                changes -= 1
                changed.remove(left)
                
            left += 1
            
    ans.append(changes)

    
    f = 'RGB' * (k // 3)
    s = 'GBR' * (k // 3)
    tr = 'BRG' * (k // 3)
    
    if k > 2 and (f in  b or s in b or tr in b):
        print(0)
    else:
        print(min(ans))
             