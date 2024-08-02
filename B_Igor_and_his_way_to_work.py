import threading
from sys import stdin,stdout,setrecursionlimit
from collections import defaultdict
setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def main():
    # Enter your code here
    pass


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()