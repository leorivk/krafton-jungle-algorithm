N, r, c = map(int, input().split())
d = [[0] * (2**N) for _ in range(2**N)]
cnt = 0

def z_order(x, y, size):
    global cnt
    if size == 1:
        d[x][y] = cnt
        cnt += 1
        return
    half = size // 2
    z_order(x, y, half)
    z_order(x, y + half, half)
    z_order(x + half, y, half)
    z_order(x + half, y + half, half)

z_order(0, 0, 2**N)
print(d[r-1][c-1])

def z_order(n, r, c):
    if n == 0:
        return 0
    half = 2**(n-1)
    half_area = half * half
    if r < half and c < half:
        return z_order(n-1, r, c)
    elif r > half and c < half:
        return half_area + z_order(n-1, r, c-half)
    elif r < half and c > half:
        return 2 * half_area + z_order(n-1, r-half, c)
    else:
        return 3 * half_area + z_order(n-1, r-half, c-half)

N, r, c = map(int, input().split())
print(z_order(N, r, c))