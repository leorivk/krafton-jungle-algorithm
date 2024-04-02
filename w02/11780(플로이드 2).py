n = int(input())
m = int(input())

INF = float("inf")
table = [[INF] * n for _ in range(n)]
nxt = [[0] * n for _ in range(n)]

for i in range(n):
    table[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    if table[start-1][end-1] > cost:
        table[start-1][end-1] = cost
        nxt[start-1][end-1] = end-1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][j] > table[i][k] + table[k][j]:
                table[i][j] = table[i][k] + table[k][j]
                nxt[i][j] = nxt[i][k]

# 비용 출력
for i in range(n):
    for j in range(n):
        print(table[i][j] if table[i][j] != INF else 0, end=" ")
    print() # 다음 줄

# 경로 추적 및 출력
for i in range(n):
    for j in range(n):
        if table[i][j] == 0 or table[i][j] == INF:
            print(0)
        else:
            route = []
            current = i
            while current != j:
                route.append(current + 1)
                current = table[current][j]
            route.append(j + 1)
            
            print(len(route), *route)

