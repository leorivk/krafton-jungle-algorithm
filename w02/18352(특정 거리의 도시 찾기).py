import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

roads = [list(map(int, input().split())) for _ in range(m)]

INF = float("inf")
adj = [[] for _ in range(0, n)]

for i, j in roads:
    adj[i-1].append((1, j-1))

def dijkstra(start, n, adj):
    pq = []
    table = [INF] * n
    table[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        min_cost, min_node = heapq.heappop(pq)
        if min_cost < table[min_node]:
            continue
        
        for cost, node in adj[min_node]:
            if table[node] > cost + min_cost:
                table[node] = cost + min_cost
                heapq.heappush(pq, (table[node], node))
        
    return table

table = dijkstra(x - 1, n, adj) 

found = False
for idx, distance in enumerate(table):
    if distance == k:
        print(idx + 1) 
        found = True

if not found:
    print(-1)