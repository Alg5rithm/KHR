import math
import itertools
def solution(numbers):
    answer = 0
    
    # 에라토스테네스의 체 사용해서 소수 판별
    num = 9999999   
    array = [True for _ in range(num+1)]
    
    array[0] = False
    array[1] = False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if array[i]:
            j = 2
            while i * j <= num:
                array[i*j] = False
                j += 1
    
    arr = list(map(int, list(numbers)))

    # 순열 이용 -> 모든 가능한 경우 조사
    for i in range(1, len(numbers)+1):
        temp = list(itertools.permutations(numbers, i))
        arr = list(map(int, map(''.join, temp)))
        for val in set(arr):
            if array[val]:
                array[val] = False
                answer += 1
    return answer
