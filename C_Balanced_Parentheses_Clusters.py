# from collections import defaultdict


t = int(input())

# print(n)


def find(x):
    while x != parent[x]:
        
        parent[x] = parent[parent[x]]
        x = parent[x]
        
    return x




for _ in range(t):
    n = int(input())
    
    brackets = input()
    parent = [_ for _ in range(2 * n)]
    
    opens = []
    closes = []
    
    for i in range(2 * n):
        if brackets[i] == ')':
            a = i
            b = opens.pop()
            roota = find(a)
            rootb = find(b)
            parent[rootb] = roota
            
            
            if closes:
                c = closes.pop()
            closes.append(i)
        else:
            if closes :
                a = i
                b = closes.pop()
                roota = find(a)
                rootb = find(b)
                
                parent[rootb] = roota
                
            opens.append(i)
            
    # print(balanced)
    for i in range(2 * n):
        parent[i] = find(i)
    
    # print(parent)
    print(len(set(parent)))
                    
            
            
    