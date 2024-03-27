##
n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def matrix_mul(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += (a[i][k] * b[k][j])
            
            result[i][j] = sum % 1000
    return result

def matrix_sq(matrix, b):
    if b == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] %= 1000
        return matrix
    half = matrix_sq(matrix, b // 2)
    if b % 2 == 0:
        return matrix_mul(half, half)
    else:
        return matrix_mul(matrix_mul(half, half), matrix)

for i in matrix_sq(matrix, b):
    print(*i)