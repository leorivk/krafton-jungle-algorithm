t = int(input())

for i in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    m = int(input())

    d = [0] * (m+1)
    d[0] = 1

    for val in vals:
        for k in range(val, m+1):
            d[k] = d[k] + d[k-val]

    print(d[m])