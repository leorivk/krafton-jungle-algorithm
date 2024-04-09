import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 1000001
# d = [0] * n 으로 하면 아래 두 줄에서 인덱스 에러남
d[1] = 1
d[2] = 2

for i in range(3,n+1):
    d[i] = (d[i-1]+ d[i-2])%15746
print(d[n])