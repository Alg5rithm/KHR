n = int(input())
m = int(input())
if m == 0:
    print(min(len(str(n)), abs(n-100)))
else:
    broken = set(map(int, input().split()))
    origin = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    buttons = origin - broken

    chanel = abs(n-100)
    for i in range(1000000):
        s = str(i)
        l = len(s)
        isBreak = False
        for j in range(0, l):
            if int(s[j]) not in buttons:
                isBreak = True
                break
        if not isBreak:
            m = abs(n - i) + l
            chanel = min(chanel, m)
    print(chanel)
