from collections import deque

def bfs(grid, x, y):
    n = len(grid)
    m = len(grid[0])
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    que = deque([(x, y)]) 
    grid[x][y] = 0  # 방문 표시
    area = 1 

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 0    # 방문 표시
                que.append((nx, ny))
                area += 1

    return area

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

count = 0
max_area = 0

# 다음 그림 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            count += 1
            max_area = max(max_area, bfs(grid, i, j))

print(count)
print(max_area)

