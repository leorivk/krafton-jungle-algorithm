n = int(input())
m = int(input())

# 간선이 존재하지 않는 경우는 무한대로 설정하기 위해 초기값 무한대로 설정
INF = float("inf")
table = [[INF] * n for _ in range(n)]

# 자기 자신으로의 거리는 0
for i in range(n):
    table[i][i] = 0
    
for _ in range(m):
    start, end, cost = map(int, input().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    if table[start-1][end-1] > cost:
        table[start-1][end-1] = cost

'''
k -> i -> j 로 하는 이유?
1번을 거치는 경우 -> 모든 정점 탐색 (i, j)
2번을 거치는 경우 -> 모든 정점 탐색 i, j)
...
'''
for k in range(n):
    for i in range(n):
        for j in range(n):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])
            '''
            if table[i][j] > table[i][k] + table[k][j]:
                table[i][j] = table[i][k] + table[k][j]
            
            min -> 매번 대입이 일어나게 됨
            연산보다 대입이 느리기 때문에 갱신이 필요할 때마다 대입이 이루어지도록 하는 것이 더 빠르다
            '''

        
for i in range(n):
    for j in range(n):
        # 얘는 왜 필요?
        if table[i][j] == INF:
            print(0, end=' ')
        else:
            print(table[i][j], end=' ')
    print()