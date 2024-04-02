from collections import deque

def dfs(adj_list, v, visited):
    visited[v] = True
    result = [v]

    for next in sorted(adj_list[v]):
        if not visited[next]:
            result += dfs(adj_list, next, visited)
    
    return result

def bfs(adj_list, v, visited):
    queue = deque([v])
    visited[v] = True
    result = [v]
    
    while queue:
        cur = queue.popleft()
        for next in sorted(adj_list[cur]):
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                result.append(next)
    
    return result

n, m, v = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(m)]
adj_list = {i+1 : [] for i in range(n)}

for i, j in inputs:
    adj_list[i].append(j)
    adj_list[j].append(i)

visited = [False] * (n+1)
print(*dfs(adj_list, v, visited.copy()))

visited = [False] * (n+1)
print(*bfs(adj_list, v, visited))
