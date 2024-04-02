from collections import deque

def bfs(maze, start_x, start_y):
    n = len(maze)
    m = len(maze[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 이동 거리 누적
                queue.append((nx, ny))

    return maze[n-1][m-1]  # 모든 칸에 해당 지점까지 이동했을 때 움직인 거리 저장
                
n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]
print(bfs(maze, 0, 0))
            
    