from collections import deque

n, m, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    q = deque()

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomatoes[i][j][k] == 1:
                    q.append((j, k, i, 0))

    days = 0
    while q:
        x, y, z, cnt = q.popleft()
        days = max(days, cnt)
        for l in range(6):
            nx, ny, nz = x + dx[l], y + dy[l], z + dz[l]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomatoes[nz][nx][ny] == 0:
                tomatoes[nz][nx][ny] = 1
                q.append((nx, ny, nz, cnt + 1))

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomatoes[i][j][k] == 0:  # 안 익은 것이 있으면
                    return -1
    return days


print(bfs())

