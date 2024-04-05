from collections import deque

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    hog = deque()
    water = deque()
    visited = set()

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "S":
                hog.append((i, j, 0))
            if grid[i][j] == "*":
                water.append((i, j))

    while hog:
        for _ in range(len(water)):
            wx, wy = water.popleft()
            for i in range(4):
                new_wx, new_wy = wx + dx[i], wy + dy[i]
                if 0 <= new_wx < r and 0 <= new_wy < c and grid[new_wx][new_wy] == '.':
                    grid[new_wx][new_wy] = '*'
                    water.append((new_wx, new_wy))

        for _ in range(len(hog)):
            hx, hy, cnt = hog.popleft()
            for i in range(4):
                new_hx, new_hy = hx + dx[i], hy + dy[i]
                if 0 <= new_hx < r and 0 <= new_hy < c:
                    if (new_hx, new_hy) not in visited:
                        if grid[new_hx][new_hy] == 'D':
                            return cnt + 1
                        elif grid[new_hx][new_hy] == '.':
                            grid[new_hx][new_hy] = 'S'
                            hog.append((new_hx, new_hy, cnt + 1))
                            visited.add((new_hx, new_hy))

    return "KAKTUS"


print(bfs())

'''
고슴도치는 물이 찰 예정인 칸으로 이동할 수 없으므로 물 먼저 사이클
'''