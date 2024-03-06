from collections import deque, Counter
x = list(input())

count = Counter(x)
mini, lenght = sorted(count.items())[0]
# print(mini, lenght)

# mini = y[0]
s = deque(x)
t = []


u = []
for _ in range(lenght):
    while s[0] != mini :
        t.append(s.popleft())
    
    t.append(s.popleft())
    u.append(t.pop())

# print(s, t, u)

while s:
    # if t and s[0] > t[-1]:
    #     u.append(t.pop())
    # else:
    t.append(s.popleft())
        
        
while t:
    u.append(t.pop())
    
print("".join(u))