import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
    
def pre_to_post(pre):
    if len(pre) == 0:
        return
    '''
    전위 순회의 특성 (루트보다 작은 값들이 왼쪽, 큰 값들이 오른쪽)
    '''
    
    left, right = [], []
    root = pre[0]
    
    for i in range(1, len(pre)):
        if pre[i] > root:
            left = pre[1:i]
            right = pre[i:]
            break
    else:
        left = pre[1:]
    
    pre_to_post(left)
    pre_to_post(right)
    print(root)

pre_to_post(pre)