import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
s = []
max_val = - int(1e9)
min_val = int(1e9)


def dfs(ops, result, idx):
    global min_val, max_val
    if idx == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    if ops[0]:
        ops[0] -= 1
        dfs(ops, result+numbers[idx], idx+1)
        ops[0] += 1
    if ops[1]:
        ops[1] -= 1
        dfs(ops, result-numbers[idx], idx+1)
        ops[1] += 1
    if ops[2]:
        ops[2] -= 1
        dfs(ops, result*numbers[idx], idx+1)
        ops[2] += 1
    if ops[3]:
        ops[3] -= 1
        dfs(ops, int(result / numbers[idx]), idx+1)
        ops[3] += 1


dfs(operators, numbers[0], 1)
print(max_val)
print(min_val)