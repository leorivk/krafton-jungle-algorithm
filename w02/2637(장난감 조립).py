# # 시간 초과
# import sys

# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# gears = [list(map(int, input().split())) for _ in range(m)]

# adj = [[] for _ in range(n+1)]
# parts = set()
# for x, y, k in gears:
#     adj[x].append((y, k))
#     parts.add(y)

# root = 0
# for i in range(1, n+1):
#     if i not in parts:
#         root = i

# # 단방향이라 방문처리 할 필요 X

# total = {}

# def dfs(node, multiplier):
#     if not adj[node]:
#         total[node] = total.get(node, 0) + multiplier
#     for end, cnt in adj[node]:
#         dfs(end, multiplier * cnt)


# dfs(root, 1)

# for part, quantity in sorted(total.items()):
#     print(f"{part} {quantity}")

#######################################################################
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

adj = [[] for _ in range(n+1)]
gears = [[0] * (n+1) for _ in range(n+1)]

indegree = [0] * (n + 1)

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    adj[y].append((x, k))
    indegree[x] += 1

queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
    
while queue:
    current = queue.popleft()
    for next, quan in adj[current]:
        if gears[current].count(0) == n + 1:    # 처음엔 다 0이므로
            gears[next][current] += quan
        else:
            for i in range(1, n+1):
                gears[next][i] += gears[current][i] * quan
        
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for i in enumerate(gears[n]):
    if i[1] > 0:
        print(*i)