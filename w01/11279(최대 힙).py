'''
힙 (우선순위 큐)
'''
import sys
import heapq

n = int(input())
heap = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,(-1)*a)