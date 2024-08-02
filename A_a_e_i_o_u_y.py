n = int(input())
word = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
stack = []
for ch in word:

    if stack and  ch in vowels and stack[-1] in vowels:
        continue
    
    stack.append(ch)
    
print("".join(stack))
