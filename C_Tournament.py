import math



import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    t  = int(input())

    newmemo = {}
    def calc(num, half):
        newstate = (num, half)
        if newstate not in newmemo:
            for _ in range(half):
                num = math.floor(num/2)
                if num == 0:break
            
            newmemo[newstate] = num
        return newmemo[newstate]


    def find(array, k):
        
        memo = {}
        def dp(i, half):
            if i >= len(array):
                return 0
            
            state = (i, half)
            if state not in memo:
                
                memo[state] = max(
                    dp(i + 1, half) + calc(array[i], half) - k,
                    dp(i + 1, half + 1) + calc(array[i], half) // 2,                
                )
            return memo[state]
        return dp(0, 0)




    for _ in range(t):
        n, m = list(map(int, input().split()))
        p = list(map(int, input().split()))
        
        ans = find(p, m)
        print(ans)




if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    
    threading.stack_size(1 << 27)
    

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



