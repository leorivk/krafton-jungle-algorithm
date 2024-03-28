'''
완전 탐색
아직 미해결
'''
n = int(input())
locals = [list(map(int, input().split())) for _ in range(n)]

heights = []
for i in locals:
    for j in i:
        if j not in heights:
            heights.append(j)

heights.sort()
