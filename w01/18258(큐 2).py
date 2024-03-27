##
import sys
from collections import deque

'''
list -> deque, sys.stdin.readline 사용하여 시간 단축 (or 시간 초과)
'''

input = sys.stdin.readline
n = int(input())

que = deque()

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == "push":
        que.append(cmd[1])
    elif cmd[0] == "pop":
        print(-1 if len(que) == 0 else que.popleft())
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        print(1 if len(que) == 0 else 0)
    elif cmd[0] == "front":
        print(-1 if len(que) == 0 else que[0])
    elif cmd[0] == "back":
        print(-1 if len(que) == 0 else que[-1])
            
