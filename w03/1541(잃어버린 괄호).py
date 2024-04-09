calc = input().split("-")

result = 0
for i, group in enumerate(calc):
    parts = group.split("+")
    sum_parts = sum(map(int, parts))
    if i == 0:
        result += sum_parts
    else:
        result -= sum_parts

print(result)
