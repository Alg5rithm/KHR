def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    result = 1
    temp_x = x
    temp_y = 1

    # 멸망 날짜
    year = lcm(m, n)

    while True:

        if temp_x > year or (temp_x - 1) % n + 1 == y:
            break

        temp_x += m
    if temp_x > year:
        print(-1)
    else:

        print(temp_x)
