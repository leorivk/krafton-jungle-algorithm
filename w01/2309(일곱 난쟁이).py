'''
완전 탐색
dfs?
'''
import sys

input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]

found = False
# 제외할 난쟁이 완전 탐색
for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            '''
            작은 인덱스부터 제거 시 뒤 쪽 인덱스 변동
            큰 인덱스 먼저 제거
            '''
            del dwarfs[j] 
            del dwarfs[i]  
            dwarfs.sort()
            found = True
            break
    if found:
        break

for i in dwarfs:
    print(i)
    
