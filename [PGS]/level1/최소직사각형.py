def solution(sizes):
    answer = 0
    a, b = 0, 0
    # 정렬
    arr = list(map(sorted, sizes))
    for value in arr:
        a, b = max(value[0], a), max(value[1], b)
    answer = a * b
    return answer
