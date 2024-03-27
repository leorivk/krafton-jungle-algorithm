##
n, k = map(int, input().split())

arr = [i+1 for i in range(n)]

answer = []

i = 0
while arr:
    i = (i + k - 1) % len(arr)
    answer.append(arr.pop(i))

print("<", ", ".join(map(str, answer)), ">", sep='')
