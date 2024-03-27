# 모듈러 분배 법칙
##
a, b, c = map(int, input().split())

def sq(a, b, c):
    if b == 0:
        return 1
    
    half = sq(a, b//2, c) % c
    if b % 2 == 0:
        return (half ** 2) % c 
    else:
        return (half ** 2 * a) % c

print(sq(a, b, c))
