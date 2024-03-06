# a = input()


# count = 0

# stack = []
# for ch in a:
#     # print(ch)
#     # print(stack)
#     if stack and stack[-1] == ch:
#         count += 1
#         stack.pop()
#     else:
#         stack.append(ch)
        
# # print(count) 
# if count % 2 != 0:
#     print("Yes")
# else:
#     print("No")
    

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your solution here
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
