from collections import deque

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

def bfs(adj, start, n):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True

    cnt = 0
    while q:
        com = q.popleft()
        for i in adj[com]:
            if not visited[i]:
                cnt += 1
                visited[i] = True 
                q.append(i)
    return cnt

print(bfs(adj, 1, n))
