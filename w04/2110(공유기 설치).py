import sys

input = sys.stdin.readline

n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

start = 1
end = houses[-1] - houses[0]
result = 0

if n == 2:
    print(end)
else:
    # 조건을 만족하는 공유기를 설치할 집 간의 최대 거리를 이분 탐색으로 찾기
    while start <= end:
        mid = (start + end) // 2
        prev = houses[0]
        cnt = 1

        for i in range(1, n):
            if houses[i] - prev >= mid:
                prev = houses[i]
                cnt += 1
        
        if cnt >= c:
            result = mid 
            start = mid + 1
        else:
            end = mid - 1
            
    print(result)
