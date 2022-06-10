# 테트로미노 1,2,3,4,5를 다 놓는 경우.
# 테트로미노 1 : 가로, 세로 4
# 테트로미노 2 : 네모 1
# 테트로미노 3 : 8
# 테트로미노 4 : 4
# 테트로미노 5 : 4

def func1():
    # 가로
    global max_val
    for i in range(m-3):
        for j in range(n):
            val = array[j][i] + array[j][i+1] + array[j][i+2] + array[j][i+3]
            max_val = max(max_val, val)

    # 세로
    for i in range(n-3):
        for j in range(m):
            val = array[i][j] + array[i+1][j] + array[i+2][j] + array[i+3][j]
            max_val = max(max_val, val)


def func2():
    global max_val
    # 가로 이동
    for i in range(m-1):
        for j in range(n-1):
            val = array[j][i] + array[j][i+1] + array[j+1][i] + array[j+1][i+1]
            max_val = max(max_val, val)


def func3():
    global max_val
    for i in range(n-2):
        for j in range(m-1):
            val = array[i][j] + array[i+1][j] + array[i+2][j] + array[i+2][j+1]
            max_val = max(max_val, val)

    for i in range(n-2):
        for j in range(m-1):
            val = array[i+2][j] + array[i][j+1] + \
                array[i+1][j+1] + array[i+2][j+1]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i+1][j] + array[i][j] + array[i][j+1] + array[i][j+2]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i][j] + array[i+1][j] + \
                array[i+1][j+1] + array[i+1][j+2]
            max_val = max(max_val, val)

    for i in range(n-2):
        for j in range(m-1):
            val = array[i][j] + array[i][j+1] + \
                array[i+1][j+1] + array[i+2][j+1]
            max_val = max(max_val, val)

    for i in range(n-2):
        for j in range(m-1):
            val = array[i][j] + array[i+1][j] + \
                array[i+2][j] + array[i][j+1]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i+1][j] + array[i+1][j+1] + \
                array[i+1][j+2] + array[i][j+2]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i][j] + array[i][j+1] + \
                array[i][j+2] + array[i+1][j+2]
            max_val = max(max_val, val)


def func4():
    global max_val
    for i in range(n-2):
        for j in range(m-1):
            val = array[i][j] + array[i+1][j] + \
                array[i+1][j+1] + array[i+2][j+1]
            max_val = max(max_val, val)

    for i in range(n-2):
        for j in range(m-1):
            val = array[i][j+1] + array[i+1][j+1] + \
                array[i+1][j] + array[i+2][j]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i+1][j] + array[i+1][j+1] + \
                array[i][j+1] + array[i][j+2]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i][j] + array[i][j+1] + \
                array[i+1][j+1] + array[i+1][j+2]
            max_val = max(max_val, val)


def func5():
    global max_val
    for i in range(n-1):
        for j in range(m-2):
            val = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1]
            max_val = max(max_val, val)

    for i in range(n-1):
        for j in range(m-2):
            val = array[i][j+1] + array[i+1][j] + \
                array[i+1][j+1] + array[i+1][j+2]
            max_val = max(max_val, val)

    for i in range(n-2):
        for j in range(m-1):
            val = array[i+1][j] + array[i][j+1] + \
                array[i+1][j+1] + array[i+2][j+1]
            max_val = max(max_val, val)

    for i in range(n-2):
        for j in range(m-1):
            val = array[i][j] + array[i+1][j] + \
                array[i+1][j+1] + array[i+2][j]
            max_val = max(max_val, val)


n, m = map(int, input().split())

array = []
max_val = 0

for _ in range(n):
    array.append(list(map(int, input().split())))

func1()
func2()
func3()
func4()
func5()
print(max_val)
