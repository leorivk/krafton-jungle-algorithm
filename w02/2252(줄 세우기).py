# 시간 초과
'''
각 노드에서 나가는 간선 정보를 여러 번 순회하는 비효율 존재
인접 리스트를 사용하여 각 노드에서 직접 연결된 노드들을 저장하면,
각 노드에 대한 순회를 한 번만 수행하면 됨

또한, 입력이 (u, v) 형태로 주어지며 u에서 v로 가는 간선을 의미한다는 점을 고려
indegree를 계산하고, indegree가 0인 모든 노드를 큐에 추가한 다음,
큐에서 하나씩 노드를 꺼내면서 위상 정렬을 수행
'''
from collections import deque

n, m = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(m)]
indegree = [0] * (n + 1)
for i in inputs:
    indegree[i[1]] += 1 # 비교한 키 중 뒤에 있는 키 + 1

queue = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    target = queue.popleft()
    result.append(target)
    for i in inputs:
        if i[0] == target:
            indegree[i[1]] -= 1
            if indegree[i[1]] == 0:
                queue.append(i[1])

print(*result)

# 성공
from collections import deque

n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# 인접 리스트 및 진입 차수(indegree) 계산
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    indegree[v] += 1

queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])

result = []
while queue:
    cur = queue.popleft()
    result.append(cur)

    for next_node in adj_list[cur]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

print(*result)
