def solution(n,a,b):
    answer = 1
    
    while a != b:
        if a%2 == 1:
            a = a//2 + 1
        else:
            a = a//2
        if b%2 == 1:
            b = b//2 + 1
        else:
            b = b//2
        if a == b:
            break
        else:
            answer += 1

    return answer
