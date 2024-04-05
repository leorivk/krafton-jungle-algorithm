n = int(input())
a = "0" + input()
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(1, n):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    
    # 맞닿아 있는 두 정점이 실내인 경우
    if a[i] == "1" and a[j] == "1":
        cnt += 2

# 해당 정점 주변의 실내 개수를 구하는 함수
def dfs(node):
    visited[node] = True
    # 인접한 실내 정점의 개수
    inside = 0
    for v in graph[node]:
        if a[v] == "1":
            inside += 1 # 실내이므로 +1
        elif not visited[v] and a[v] == "0":    
            '''
            인접한 정점 중
            아직 방문하지 않는 실외 정점들을 대상으로 
            dfs를 수행하여 나온 결과들을 합계
            '''
            inside += dfs(v) 
    return inside

for i in range(1, n+1):
    # 시작점 : 아직 방문하지 않은 실외 정점
    if a[i] == "0" and not visited[i]:
        result = dfs(i) # 시작점으로부터 인접한 실내 정점의 개수
        cnt += (result) * (result - 1)
        
print(cnt)

'''
원래는 시작점인 실내를 기준으로 탐색

중간에 실내를 거쳐가면 안되므로
실외에 인접한 실내들만 고려 -> 실외에 초점
실외가 이어져 있어도 dfs 재귀를 통해 인접한 실내 모두 구할 수 있음 
'''