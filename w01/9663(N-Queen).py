# 시간 초과
def is_safe(arr, row, col):
    for i in range(row):
        # 같은 열, 대각선 확인
        if arr[i] == col or abs(arr[i] - col) == abs(i - row):
            return False
    return True

def nqueen(arr, row):
    global cnt, n
    if row == n:
        cnt += 1
        return
    for i in range(n):
        if is_safe(arr, row, i):
            arr.append(i)  # 현재 행에 i 열에 퀸을 배치
            nqueen(arr[:], row + 1)  # 다음 행으로 재귀 호출
            arr.pop()  # 현재 행의 퀸을 제거하고 다른 열 시도

n = int(input())  # 체스판의 크기 N 입력
cnt = 0
nqueen([], 0)
print(cnt)
