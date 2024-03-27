##
n = int(input())

def hanoi(n, start, end, other):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, other, end)
        if n <= 20:
            print(start, end)
        hanoi(n-1, other, end, start)

print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)