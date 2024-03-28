'''
이분 탐색
'''
n, m = map(int, input().split())

trees = list(map(int, input().split()))

shortest, longest = 0, max(trees)

result = 0
while shortest <= longest:
    mid = (shortest + longest) // 2

    total = sum(tree - mid if tree > mid else 0 for tree in trees)
    
    if total < m:
        longest = mid - 1
    elif total > m:
        result = mid
        shortest = mid + 1

print(result)
