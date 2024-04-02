
# 스택
'''
시간 초과
'''
def dfs(adj_list, visited, start):
    stk = []
    stk.append(start)
    visited[start] = True

    while stk:
        node = stk.pop()
        for i in adj_list[node]:
            if not visited[i]:
                stk.append(i)
                visited[i] = True

n, m = map(int, input().split())

inputs = [list(map(int, input().split())) for _ in range(m)]

adj_list = {i : [] for i in range(1, n+1)}

for i in inputs:
    # 무방향
    adj_list[i[0]].append(i[1])
    adj_list[i[1]].append(i[0])
    
visited = [False] * (n+1)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(adj_list, visited, i)
        cnt += 1

print(cnt)

# 재귀
'''
recursion error 발생
import sys
sys.setrecursionlimit(10**6)
추가해주었더니 시간 초과
'''
def dfs(adj_list, visited, node):
    visited[node] = True
    for next_node in adj_list[node]:
        if not visited[next_node]:
            dfs(adj_list, visited, next_node)

n, m = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(m)]

adj_list = {i: [] for i in range(1, n + 1)}

for u, v in inputs:
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False] * (n + 1)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(adj_list, visited, i)
        cnt += 1

print(cnt)

# 성공
'''
input()에서 sys.stdin.readline()으로만 바꿨는데 성공

입력 속도 개선: 
Python에서 많은 수의 입력을 처리할 때 input() 함수보다 sys.stdin.readline()을 사용하면 더 빠릅니다. 
단, sys.stdin.readline() 사용 시 줄 바꿈 문자도 함께 입력되므로, 문자열 처리에 주의해야 합니다.

DFS 최적화: 
DFS 함수는 이미 최적화되어 보입니다. 추가적인 최적화가 필요하다면,
알고리즘의 로직 변경보다는 구현의 효율성을 검토해야 합니다.

인접 리스트의 효율적 사용: 
인접 리스트를 만들 때, 간선 정보를 입력받는 즉시 두 노드 간의 연결을 추가합니다.
이 부분은 이미 잘 처리되고 있습니다.

재귀 대신 반복 사용: 
Python에서 깊은 재귀는 스택 오버플로우를 발생시킬 수 있으므로, 
가능하다면 재귀 대신 반복을 사용하는 방법도 고려할 수 있습니다.
그러나 이 경우 DFS 구현은 재귀적 접근이 자연스럽기 때문에,
반복적 접근이 반드시 더 나은 선택은 아닙니다.
'''
import sys
sys.setrecursionlimit(10**6)
def dfs(node, adj_list, visited):
    visited[node] = True
    for next_node in adj_list[node]:
        if not visited[next_node]:
            dfs(next_node, adj_list, visited)

n, m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False] * (n + 1)
cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, adj_list, visited)
        cnt += 1

print(cnt)
        




