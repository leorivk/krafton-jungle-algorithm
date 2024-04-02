import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

'''
현재 노드의 색상을 전달해주지 않고 1로 고정해버리면
반대되는 색상을 칠하지 못함
'''
def dfs(node, adj, color, c):
    color[node] = c
    for next_node in adj[node]:
        if color[next_node] == c:
            return False
        if color[next_node] == 0:
            if not dfs(next_node, adj, color, -c):
                return False
    return True

'''
그래프가 연결되어 있지 않은 경우,
즉 연결 리스트가 아닌 경우
dfs를 한 번만 호출하면 그래프의 일부만 탐색
그래프의 모든 노드를 커버하기 위해서는 각 연결 요소에 대해 dfs 호출 필요
'''

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (V + 1)
    is_bipartite = "YES"
    for node in range(1, V + 1):
        if color[node] == 0:
            if not dfs(node, adj, color, 1):
                is_bipartite = "NO"
    print(is_bipartite)
