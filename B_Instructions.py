import sys, threading


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().split()))
    
        memo = {}
        def move(idx, selected):
            if idx >= n:return 0
            
            # print('count')
            state = (idx, selected)
            if state not in memo:
                if selected:
                    memo[state] = move(idx + array[idx], selected)+ array[idx]
                else:
                    memo[state] = max(move(idx + 1, selected), move(idx + array[idx], True) + array[idx])
            return memo[state]
   
        print(move(0, False))
    

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    answer = [array[i] for i in range(n)]
    
    for i in range(n):
        if i + array[i] < n:
            answer[i + array[i]] = max(answer[i + array[i]], array[i + array[i]] + answer[i])
            
    print(max(answer))