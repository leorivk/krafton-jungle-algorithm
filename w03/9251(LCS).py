A = [i for i in input()]
B = [i for i in input()]


n = len(A)
m = len(B)
d = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else :
            d[i][j] = max(d[i-1][j], d[i][j-1])

print((d[n][m]))

