import sys
input = sys.stdin.readline
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

d = [[0 if i == j else int(1e9) for j in range(n)] for i in range(n)]

for length in range(1, n): # 부분 행렬 곱의 길이
    for i in range(n - length): # 시작점 위치
        for k in range(i, i + length): # 중간점 위치
             # matrix[k][1]도 되고 matrix[k+1][0]도 됨
            d[i][i + length] = min(d[i][i + length],
                                   d[i][k] + d[k+1][i+length]
                                   + matrix[i][0] * matrix[k][1] * matrix[i+length][1])
            
print(d[0][n-1])
