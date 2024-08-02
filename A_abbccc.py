n = int(input())

s = input()

pointer = 0
add = 1
answer = []
while pointer < n:
    answer.append(s[pointer])
    pointer += add
    add += 1
    
print("".join(answer))