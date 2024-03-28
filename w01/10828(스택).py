import sys

n = int(sys.stdin.readline())

stk = []

for _ in range(n):
    input = sys.stdin.readline().split()
    cmd = input[0]
    
    if cmd == "push":
        stk.append(input[1])
    elif cmd == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
    elif cmd == "size":
        print(len(stk))
    elif cmd == "empty":
        print(1 if len(stk) == 0 else 0)
    elif cmd == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())

