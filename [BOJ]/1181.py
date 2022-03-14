n = int(input())

li=[]
for _ in range(n):
    s = input()
    if s not in li :

        li.append(s)
li.sort(key= lambda x: (len(x), x))

for i in li:
    print(i)
