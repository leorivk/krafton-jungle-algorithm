import heapq

def prim(graph, v):
    # graph : (시작 노드, 도착 노드, 가중치)
    # 인접 리스트 형태로 생성
    adj_list = {i: [] for i in range(1, v+1)}
    for start, end, w in graph:
        # 무방향 그래프
        adj_list[start].append((w, end))  # start번째 노드의 도착지는 end이고 가중치는 w
        adj_list[end].append((w, start))  # end번째 노드의 도착지는 u이고 가중치는 w

    # visited = [False] * (v + 1)  # 각 노드의 방문 여부
    pqueue = [(0, 1)]  # 가중치 0, 시작노드 1
    visited = set()  # 선택된 정점들
    mst_cost = 0  # MST의 총 가중치


    while pqueue and len(visited) < v:
        w, current = heapq.heappop(pqueue)
        
        if current in visited:  # 현재 노드가 이미 방문한 노드일 경우
            continue
        
        visited.add(current)  # 방문한 노드 목록에 추가 
        mst_cost += w  # 총 가중치에 가중치 합산
        
        for adj_w, adj_node in adj_list[current]:  # 현재 노드와 연결된 모든 노드를 탐색
            if adj_node not in visited:
                heapq.heappush(pqueue, (adj_w, adj_node))
    
    return mst_cost


v, e = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(v)]
mst_cost = prim(graph, v)
print(mst_cost)
