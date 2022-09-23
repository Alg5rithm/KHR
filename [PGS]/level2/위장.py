def solution(clothes):
    answer = 1
    d = dict()
    for a, b in clothes:
        d[b] = d.get(b, 0) + 1
    
    for a in d:
        answer *= (d[a] + 1)
    
    return answer - 1
