n, k = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(n)]

d = [0] * (k+1)

for w, v in stuff:
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w] + v)

print(d[k])