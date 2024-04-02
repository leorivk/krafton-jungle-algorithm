import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
    
n = int(input())

tree = [list(map(int, input().split())) for _ in range(n-1)]

adj = [[] for _ in range(n+1)]

for i, j in tree:
    adj[i].append(j)
    adj[j].append(i)

visited = [False] * (n+1)
result = [0] * (n+1)

def dfs(start, adj, visited, result):
    visited[start] = True
    for i in adj[start]:
        if not visited[i]:
            result[i] = start  # 재귀 호출 전에 부모를 기록
            dfs(i, adj, visited, result)

dfs(1, adj, visited, result)

# 0번은 생략, 1번은 루트 -> 2번째 요소부터 출력
for i in range(2, n+1):
    print(result[i])
