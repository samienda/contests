from collections import Counter


t = int(input())


for _ in range(t):
    
    letters = input()
    
    count = Counter(letters)
    red = 0
    green = 0
        
    for ch in count:
        j = 0 
        for i in range(count[ch]):
            if j >= 2 : break
            
            if red > green:
                green += 1
            else:
                red += 1
            j += 1
            
    print(min(red, green))
                
        
        
        
        