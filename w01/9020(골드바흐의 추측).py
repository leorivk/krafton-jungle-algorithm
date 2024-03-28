import sys
n = int(sys.stdin.readline())
test = [int(input()) for _ in range(n)]

def primes(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:    
            for j in range(i+i, n, i): 
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

max = max(test)
primes = primes(max)

for num in test:
    for i in range(2, num // 2 + 1):
        '''for문을 돌며 최종적으로 가장 큰 소수인 i값을 탐색하므로 차이에 대한 고민할 필요 X'''
        if i in primes and (num - i) in primes:
            print(i, num - i)
    
    