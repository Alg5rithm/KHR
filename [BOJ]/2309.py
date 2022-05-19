from itertools import combinations
arr = []

for _ in range(9):
    arr.append(int(input()))

temp = list(combinations(arr, 7))
result = ()
for val in temp:
    if sum(val) == 100:
        result = val
        break

for val in sorted(result):
    print(val)
