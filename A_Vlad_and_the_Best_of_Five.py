t = int(input())
from collections import Counter

for _ in range(t):
    
    a = input()
    
    count = Counter(a)
    
    if count['A'] > count['B']:
        print('A')
    else:
        print('B')