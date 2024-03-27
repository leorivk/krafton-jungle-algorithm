import sys

input = sys.stdin.readline

n = int(input())

'''
그냥 input() 사용 시 시간 초과
시간 줄이는 법?
'''

arr = [int(input()) for _ in range(n)]

arr.sort()

for i in arr:
    print(i)

