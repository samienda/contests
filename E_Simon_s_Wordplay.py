t = int(input())
from collections import Counter

def find(ch, words, dic, len_words, n):
    adif = []
    for i in range(n):
        length = len_words[i]
        a = Counter(words[i])[ch]
        adif.append([length - (2 * a), i])
        
    compare = [dic[ch], sum(len_words) - dic[ch]]
    adif.sort()
    
    while adif and compare[0] <= compare[1]:
        _, idx = adif.pop()
        word = words[idx]
        
        a = Counter(word)[ch]
        compare[0] -= a
        compare[1] -= (len(word) - a)
        
    return len(adif)




for _ in range(t):
    n = int(input())
    words = []
    len_words = []
    dic = Counter()
    # print(dic)
    for _ in range(n):
        
        s = input()
        dic += Counter(s)
        words.append(s)
        len_words.append(len(s))
        
    ans = [find(ch, words, dic, len_words, n) for ch in 'abcde']
    print(max(ans))
    
    

    