t = int(input())

target = "codeforces"


for i in range(t):
    
    word = input()
    
    count = 0
    for i in range(10):
        if target[i] != word[i]:
            count += 1
            
    print(count)