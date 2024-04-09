n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

d = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]

for length in range(1, n):
    for i in range(n - length):
        j = i + length
        for k in range(i, j):
            cost = d[i][k] + d[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            d[i][j] = min(d[i][j], cost)

print(d[0][n-1])
