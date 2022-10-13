from itertools import permutations
n, m = map(int, input().split())
li = [i for i in range(1, n+1)]
result = list(permutations(li, m))

for value in result:
  for i in value:
    print(i,end=' ')
  print()
