'''
분할 정복
'''
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def cut(x, y, n):
    global white, blue
    temp = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j]:
                temp += 1
    
    if not temp:
        white += 1
    elif temp == n ** 2:
        blue += 1
    else:
        cut(x, y, n // 2)
        cut(x + n // 2, y, n // 2)
        cut(x, y + n // 2, n // 2)
        cut(x + n // 2, y + n // 2, n // 2)
    return

cut(0, 0, n)
print(white)
print(blue)

    