from collections import Counter


n, k =  list(map(int, input().split()))

string = input()
count = Counter(string)

mini = float('inf')
for i in range(k):
    mini =min(mini, count[chr(ord('A') + i)])
    
print(mini * k)

