'''
스택
'''
import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

stk = []
answer = [0] * n # 모든 요소를 0으로 초기화

for i in range(len(towers)):
    # 스택이 비거나 현재 타워의 값보다 스택의 꼭대기값이 더 클 때까지 루프
    while stk and towers[i]> stk[-1][1] :
        stk.pop()
    
    # 스택에 값이 남아있는 경우 : 스택의 꼭대기 값이 현재 타워의 값보다 큰 경우
    # 해당 경우에만 값 변경
    if stk:
        answer[i] = stk[-1][0]
    
    stk.append((i+1, towers[i]))

print(*answer)
