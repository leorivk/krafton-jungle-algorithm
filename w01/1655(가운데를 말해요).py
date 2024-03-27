##
import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heap = []  # 최대 힙
min_heap = []  # 최소 힙

for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:  # 최대 힙의 루트가 최소 힙의 루트보다 클 경우
        max_val = heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, -max_val)

    print(-max_heap[0])