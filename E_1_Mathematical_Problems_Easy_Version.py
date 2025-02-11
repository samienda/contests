t = int(input())
outputs = [100, 200, 0]
for _ in range(t):
    x = int(input())
    print(outputs[x % 3])  
