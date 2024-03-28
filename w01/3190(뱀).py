'''
큐, 시뮬레이션
'''
n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
apples = [tuple(map(int, input().split())) for _ in range(k)]  # 사과의 위치

l = int(input())  # 뱀의 방향 변환 횟수
directions = [input().split() for _ in range(l)]
directions = [(int(x), y) for x, y in directions]  # (시간, 방향)

# 방향: 오른쪽(R), 아래(D), 왼쪽(L), 위(U)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 처음에 오른쪽을 향함

time = 0
x, y = 1, 1  # 뱀의 시작 위치
snake = [(x, y)]  # 뱀이 차지하고 있는 위치 정보

for t, d in directions + [(10001, '')]:  # 마지막으로 뱀이 벽에 부딪히는 경우를 고려하여 (10001, '') 추가
    while time < t:
        time += 1
        x += dx[direction]
        y += dy[direction]
        if (x < 1 or x > n or y < 1 or y > n or (x, y) in snake):
            print(time)
            exit(0)
        if (x, y) in apples:
            apples.remove((x, y))
        else:
            snake.pop(0)
        snake.append((x, y))
    if d == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
