n = int(input())
liq = list(map(int, input().split()))

liq.sort()

min_diff = 2e+9+1
answer = []  

i, j = 0, n-1

while i < j:
    current_sum = liq[i] + liq[j]
    if current_sum == 0:
        answer = [liq[i], liq[j]]
        break  
    
    if abs(current_sum) < min_diff:
        min_diff = abs(current_sum)
        answer = [liq[i], liq[j]]
    
    if current_sum > 0:
        j -= 1  
    else:
        i += 1  


print(*answer)

        
