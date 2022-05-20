def column(l, arr):
    max_val = 1
    temp = ''
    for i in range(l):
        count = 1
        temp = arr[0][i]
        for j in range(1, l):
            if arr[j][i] == temp:
                count += 1
                max_val = max(count, max_val)
            else:
                temp = arr[j][i]
                count = 1

        if max_val == l:
            return max_val

    return max_val


def row(l, arr):
    max_val = 1
    temp = ''
    for i in range(l):
        count = 1
        temp = arr[i][0]
        for j in range(1, l):
            if arr[i][j] == temp:
                count += 1
                max_val = max(count, max_val)
            else:
                temp = arr[i][j]
                count = 1

        if max_val == l:
            return max_val

    return max_val


def func(l, arr):
    result = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(l):
        for j in range(l):
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < l and 0 <= y < l:
                    arr[i][j], arr[x][y] = arr[x][y], arr[i][j]
                    result = max(result, column(l, arr), row(l, arr))
                    if result == l:
                        return result
                    arr[i][j], arr[x][y] = arr[x][y], arr[i][j]
    return result


n = int(input())

bomboni = []

for _ in range(n):
    bomboni.append(list(input()))

print(func(n, bomboni))
