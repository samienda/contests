t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    a = [ord(ch) - ord('a') + 1 for ch in s]
    
    print(max(a))