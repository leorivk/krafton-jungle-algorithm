import heapq

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

visited = [[False] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    visited[0][0] = True

    while pq:
        cnt, x, y = heapq.heappop(pq)
        if x == n - 1 and y == n - 1:
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maze[nx][ny] == 1:
                    heapq.heappush(pq, (cnt, nx, ny))
                else:
                    heapq.heappush(pq, (cnt + 1, nx, ny))
                visited[nx][ny] = True

print(bfs())
