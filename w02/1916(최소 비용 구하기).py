import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, n, adj):
    pq = []
    INF = float("inf")
    table = [INF] * (n+1)
    table[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        m_cost, m_node = heapq.heappop(pq)
        if table[m_node] != m_cost:
            continue
        
        for cost, node in adj[m_node]:
            if table[node] > cost + m_cost:
                table[node] = cost + m_cost
                heapq.heappush(pq, (table[node], node))
    return table

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    adj[start].append((cost, end))

t_start, t_end = map(int, input().split())

table = dijkstra(t_start, n, adj)
print(table[t_end])