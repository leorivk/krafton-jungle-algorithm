##
import itertools

n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

# 도시 i에서 j로 갈 수 없는 경우, 비용을 무한대로 설정
for i in range(n):
    for j in range(n):
        if costs[i][j] == 0 and i != j:
            costs[i][j] = float('inf')

permutations = itertools.permutations(range(n))

min_cost = float('inf')  

for perm in permutations:
    cost_sum = 0
    
    for i in range(n-1):
        cost_sum += costs[perm[i]][perm[i+1]]
    
    cost_sum += costs[perm[-1]][perm[0]]

    if min_cost > cost_sum:
        min_cost = cost_sum


print(min_cost)