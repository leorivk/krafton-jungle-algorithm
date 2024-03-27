n = int(input())
arr1 = set(map(int, input().split())) # list 대신 set
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    print(1 if i in arr1 else 0)