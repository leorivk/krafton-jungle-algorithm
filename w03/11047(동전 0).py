n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0

for i in range(len(coins)-1, -1, -1):
    coin = coins[i]
    if coin > k:
        continue

    cnt += k // coin
    k %= coin

    if k == 0:
        break

print(cnt)